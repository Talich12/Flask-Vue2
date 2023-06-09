import math
from app import app, db, jwt
from flask import jsonify, request, g
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from app.models import User, Post, Genre, Likes, Comments, SavedPost, RevokedTokenModel, PostSchema, UserSchema ,GenreSchema, SavedPostSchema, CommentsSchema,followers
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
from urllib.parse import urlparse, parse_qs
import os
import time
import json
from gtts import gTTS

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def get_index():
    post_schema = PostSchema(many=True)
    data = request.get_json(silent=True)
    output = {}

    filters = []

    value = int(data['value'])
    page = data['page']
    video = data['video']
    audio = data['audio']
    curse = data['curse']
    violence = data['violence']

    if video:
        filters.append(getattr(Post, 'has_video') == video)
    if audio:
        filters.append(getattr(Post, 'has_audio') == audio)
    if curse:
        filters.append(getattr(Post, 'has_curse') == curse)
    if violence:
        filters.append(getattr(Post, 'has_violence') == violence)


    if  filters == {}:
        req = Post.query.order_by(Post.timestamp.desc())
    else:
        req = Post.query.filter(*filters).order_by(Post.timestamp.desc())



    posts = req.paginate(page=page,per_page=value,error_out=False)
    output_query = post_schema.dump(posts)
    len = req.count()
    len =  math.ceil(len/value)
    output["data"] = output_query
    output["len"] = len
    return jsonify(output)


@app.route('/post/<id>', methods=['GET'])
def get_post(id):
    output = {}
    post_schema = PostSchema(many= False)
    comments_schema = CommentsSchema(many = True)
    post = Post.query.filter_by(id=id).first()

    comments = Comments.query.filter_by(post_id = id).order_by(Comments.timestamp.desc())
    output['post'] = post_schema.dump(post)
    output['comments'] = comments_schema.dump(comments)

    return jsonify(output)


@app.route('/post/like', methods=['POST'])
@jwt_required(refresh=False)
def post_like():
    data = request.get_json()
    post_id = int(data['post_id'])
    login = get_jwt_identity()

    find_user = User.query.filter_by(username = login).first()
    find_post = Post.query.filter_by(id = post_id).first()

    find_like = Likes.query.filter_by(user_id = find_user.id, post_id = post_id).first()

    if find_like != None:
        db.session.delete(find_like)
        find_post.like_count -= 1
        db.session.commit()
        return jsonify({"Status" : "delete_like"})

    like = Likes(user_id = find_user.id, post_id = post_id, user = find_user, post = find_post)
    find_post.like_count += 1

    db.session.add(like)
    db.session.commit()


    return jsonify({'Status': "add_like"})

@app.route('/post/comment', methods=['POST'])
@jwt_required(refresh=False)
def post_comment():
    data = request.get_json()
    post_id = int(data['post_id'])
    text = data['text']
    login = get_jwt_identity()

    find_user = User.query.filter_by(username = login).first()
    find_post = Post.query.filter_by(id = post_id).first()

    comment = Comments(user_id = find_user.id, post_id = post_id, user = find_user, post = find_post, text = text)

    db.session.add(comment)
    db.session.commit()

    return jsonify({'Status': "add_comment"})

@app.route('/post/save', methods=['POST'])
@jwt_required(refresh=False)
def post_save():
    data = request.get_json()
    post_id = int(data['post_id'])
    login = get_jwt_identity()

    find_user = User.query.filter_by(username = login).first()
    find_post = Post.query.filter_by(id = post_id).first()

    find_save = SavedPost.query.filter_by(user_id = find_user.id, post_id = post_id).first()
    if find_save != None:
        return jsonify({'Status': "save_exist"})

    save = SavedPost(user_id = find_user.id, post_id = post_id, user = find_user, post = find_post)

    db.session.add(save)
    db.session.commit()

    return jsonify({'Status': "add_save"})

@app.route('/post/follow', methods=['POST'])
@jwt_required(refresh=False)
def post_follow():
    data = request.get_json()
    user_id = int(data['user_id'])
    login = get_jwt_identity()

    find_user = User.query.filter_by(username = login).first()
    find_follow = User.query.filter_by(id = user_id).first()

    find_user.follow(find_follow)

    return jsonify({'Status': "add_follow"})


@app.route('/search', methods=['GET', 'POST'])
def search():
    output = {}
    data = request.get_json(silent=True)

    search = data['search']
    value = int(data['value'])
    page = int(data['page'])

    if search == "":
        posts_request = Post.query.order_by(Post.timestamp.desc())
    else:
        posts_request = Post.query.filter(Post.title.ilike(f'%{search}%')).order_by(Post.timestamp.desc())

    posts = posts_request.paginate(page=page,per_page=value,error_out=False)

    post_schema = PostSchema(many=True)
    output_query = post_schema.dump(posts)

    len = posts_request.count()
    len =  math.ceil(len/value)

    output["data"] = output_query
    output["len"] = len
    
    return jsonify(output)

@app.route('/saved', methods=['POST'])
@jwt_required(refresh=False)
def get_saved():
    output = {}
    login = get_jwt_identity()

    data = request.get_json(silent=True)
    value = int(data['value'])
    page = int(data['page'])

    find_user = User.query.filter_by(username = login).first()

    posts_request = SavedPost.query.filter_by(user_id = find_user.id).order_by(SavedPost.timestamp.desc()).paginate(page=page,per_page=value,error_out=False)

    len = SavedPost.query.filter_by(user_id = find_user.id).count()
    len =  math.ceil(len/value)

    post_schema = SavedPostSchema(many=True)
    output_query = post_schema.dump(posts_request)

    output['data'] = output_query
    output['len'] = len

    return jsonify(output)

@app.route('/followedposts', methods=['POST'])
@jwt_required(refresh=False)
def get_followed_posts():
    output = {}

    data = request.get_json(silent=True)
    value = int(data['value'])
    page = int(data['page'])
    
    login = get_jwt_identity()
    find_user = User.query.filter_by(username = login).first()

    post_schema = PostSchema(many = True)

    posts = find_user.followed_posts().order_by(Post.timestamp.desc()).paginate(page=page,per_page=value,error_out=False)

    len = find_user.followed_posts().count()
    len = math.ceil(len/value)

    output_query = post_schema.dump(posts)

    output['data'] = output_query
    output['len'] = len


    return jsonify(output)

@app.route('/profile/<username>/follow', methods=['POST'])
@jwt_required(refresh=False)
def user_follow(username):
    login = get_jwt_identity()
    find_user = User.query.filter_by(username=login).first()
    follow_user =  User.query.filter_by(username=username).first()

    find_user.follow(follow_user)

    return jsonify({'Status': "Success"})


@app.route('/profile/<username>/followers', methods=['GET'])
@jwt_required(refresh=False)
def get_followers(username):
    user_schema = UserSchema(many=True)
    login = username
    find_user = User.query.filter_by(username=login).first()
    find_followers = User.query.join(followers, (followers.c.follower_id == User.id)).filter(
                followers.c.followed_id == find_user.id)
    output = user_schema.dump(find_followers)
    return jsonify(output)

@app.route('/profile/<username>/followed', methods=['GET'])
@jwt_required(refresh=False)
def get_followed(username):
    user_schema = UserSchema(many=True)
    login = username
    find_user = User.query.filter_by(username=login).first()
    find_followers = User.query.join(followers, (followers.c.followed_id == User.id)).filter(
                followers.c.follower_id == find_user.id)
    output = user_schema.dump(find_followers)
    return jsonify(output)


@app.route('/profile/<username>/posts', methods=['GET'])
@jwt_required(refresh=False)
def get_posts(username):
    login = username
    post_schema = PostSchema(many=True)
    find_user = User.query.filter_by(username=login).first()
    posts = Post.query.filter_by(author_id=find_user.id).all()
    output = post_schema.dump(posts)
    return jsonify(output)


@app.route('/profile/<username>', methods=['GET'])
@jwt_required(refresh=False)
def get_profile(username):
    login = get_jwt_identity()
    access = False
    if username == login:
        access = True
    user_schema = UserSchema(many=False)
    find_user = User.query.filter_by(username=username).first()
    output = user_schema.dump(find_user)
    output['access'] = access
    return jsonify(output)


@app.route('/registration', methods=['POST'])
def post_register():
    data = request.get_json()
    login = data['login']
    password = data['password']
    find_user = User.query.filter_by(username=login).count()
    if find_user > 0:
        return jsonify({"status" : "Invalid username"})
    user = User(username=login)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"status" : "Success"})

@app.route('/login', methods=['POST'])
def post_login():
    data = request.get_json()
    login = data['login']
    password = data['password']
    find_user = User.query.filter_by(username=login).first()
    if find_user is None or not find_user.check_password(password):
        return jsonify({"status" : "Invalid username"})
    access_token = create_access_token(identity = login)
    refresh_token = create_refresh_token(identity = login)

    return jsonify({
        "status" : "Success",
        "access_token" : access_token,
        "refresh_token" : refresh_token
        })



@app.route('/storyadd', methods=['POST'])
@jwt_required(refresh=False)
def upload():
    data = request.form
    file = request.files['file']
    title = data['title']
    body = data['body']
    audio = data['audio']
    video = data['video']

    has_video = False
    has_audio = False
    if video != '':
        has_video = True
    if audio != '':
        has_audio = True

    genre = str(data['genre'])


    speech_filename = str(time.time()) + "_speech.mp3"
    speech = gTTS(text=body, lang="ru", slow=False)
    speech.save(os.path.join(app.config['SPEECH_FOLDER'], speech_filename))

    username = get_jwt_identity()
    filename = str(time.time()) + "_" + secure_filename(file.filename)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    find_user = User.query.filter_by(username=username).first()
    post = Post(title=title, body=body, author_id=find_user.id, author=find_user, img=filename, genre=genre, video = video, has_video = has_video, audio = audio, has_audio = has_audio, tts = speech_filename)
    db.session.add(post)
    db.session.commit()
    return jsonify({'status': "ok"})


@app.route('/genre', methods=['GET'])
def genre():
    genre_schema = GenreSchema(many=True)
    genres = Genre.query.all()
    output = genre_schema.dump(genres)
    return jsonify(output)


@app.route('/secret', methods=['GET'])
@jwt_required(refresh=False)
def secret():
    return jsonify({"status": "jenamolodec"})

@app.route('/TokenRefresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh_token():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity = current_user)
    return {'access_token': access_token}

@app.route('/LogoutAccess', methods=['GET'])
@jwt_required(refresh=False)
def logout_access():
    jti = get_jwt()['jti']
    revoked_token = RevokedTokenModel(jti = jti)
    revoked_token.add()
    return jsonify({"msg": "successsss"})

@app.route('/LogoutRefresh', methods=['GET'])
@jwt_required(refresh=True)
def logout_refresh():
    jti = get_jwt()['jti']
    revoked_token = RevokedTokenModel(jti = jti)
    revoked_token.add()
    return jsonify({"msg": "successsss"})
