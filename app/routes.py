from app import app, db, jwt
from flask import jsonify, request, g
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from app.models import User, Post, RevokedTokenModel, PostSchema
from flask_cors import cross_origin


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

@app.route('/', methods=['GET'])
@jwt_required(refresh=False)
def get_index():
    post_schema = PostSchema(many=True)
    posts = Post.query.all()
    output = post_schema.dump(posts)
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

@app.route('/CreatePost', methods=['POST'])
@jwt_required(refresh=False)
def create_post():
    data = request.get_json()
    title = data['title']
    body = data['body']
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    post = Post(title=title, body=body, author_id= user.id ,author=user)
    db.session.add(post)
    db.session.commit()
    return jsonify({"status": "Success"})