from app import app, db
from flask import jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Jena PIDORASIC!')


@app.route('/registration', methods=['GET'])
def get_register():
    if current_user.is_authenticated:
        return jsonify({"status" : "Redirect"})
    else:
        return jsonify({"status" : "Stay"})


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
    login_user(find_user)
    return jsonify({"status" : "Success"})
