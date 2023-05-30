import math
from app import app, db, jwt
from flask import jsonify, request, g
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from app.models import User, Post,Genre, RevokedTokenModel, PostSchema, UserSchema ,GenreSchema, followers
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os

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
    data = request.get_json(silent=True)
    print(data)
    value = int(data['value'])
    page = data['page']
    post_schema = PostSchema(many=True)
    posts = Post.query.paginate(page=page,per_page=value,error_out=False)
    output = post_schema.dump(posts)
    
    return jsonify(output)

@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    data = request.get_json(silent=True)
    value = int(data['value'])
    len = Post.query.count()
    len =  math.ceil(len/value)
    return jsonify({'len': len})


@app.route('/profile/<username>/follow', methods=['POST'])
def user_follow(username):
    login = "Lera"
    find_user = User.query.filter_by(username=login).first()
    follow_user =  User.query.filter_by(username=username).first()

    find_user.follow(follow_user)

    return jsonify({'Status': "success"})


@app.route('/profile/<username>/followers', methods=['GET'])
def get_followers(username):
    user_schema = UserSchema(many=True)
    login = username
    find_user = User.query.filter_by(username=login).first()
    find_followers = User.query.join(followers, (followers.c.follower_id == User.id)).filter(
                followers.c.followed_id == find_user.id)
    output = user_schema.dump(find_followers)
    return jsonify(output)

@app.route('/profile/<username>/followed', methods=['GET'])
def get_followed(username):
    user_schema = UserSchema(many=True)
    login = username
    find_user = User.query.filter_by(username=login).first()
    find_followers = User.query.join(followers, (followers.c.followed_id == User.id)).filter(
                followers.c.follower_id == find_user.id)
    output = user_schema.dump(find_followers)
    return jsonify(output)


@app.route('/profile/<username>/posts', methods=['GET'])
def get_posts(username):
    login = username
    post_schema = PostSchema(many=True)
    find_user = User.query.filter_by(username=login).first()
    posts = Post.query.filter_by(author_id=find_user.id).all()
    print(posts)
    output = post_schema.dump(posts)
    return jsonify(output)


@app.route('/profile/<username>', methods=['GET'])
def get_profile(username):
    login = "Lera"
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
    repeat_password = data['repeat_password']
    if password != repeat_password:
        return jsonify({"status" : "Password not equal"})
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


@app.route('/upload', methods=['POST'])
def upload():
    data = request.form
    file = request.files['file']
    title = data['title']
    body = data['body']
    genre_id = data['genre_id']
    print(body)
    username = 'denis'
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    find_user = User.query.filter_by(username=username).first()
    find_genre = Genre.query.filter_by(id=genre_id).first()
    post = Post(title=title, body=body, author_id= find_user.id ,author=find_user, img=filename, genre_id=genre_id, genre=find_genre)
    db.session.add(post)
    db.session.commit()
    return jsonify({'status': "ok"})


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


@app.route('/Genre', methods=['GET'])
def genre():
    genre_schema = GenreSchema(many=True)
    genres = Genre.query.all()
    output = genre_schema.dump(genres)
    return jsonify(output)


