from app import db, ma
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import fields, auto_field
from hashlib import md5
import base64
from datetime import datetime, timedelta
import os



followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64))
    avatar = db.Column(db.String(64), default="sample1.jpg")
    password_hash = db.Column(db.String(128))
    rating = db.Column(db.Integer, default=0)
    followed = db.relationship(
    'User', secondary=followers,
    primaryjoin=(followers.c.follower_id == id),
    secondaryjoin=(followers.c.followed_id == id),
    backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            db.session.commit()

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            db.session.commit()

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
    
    def followed_posts(self):
        return Post.query.join(
            followers, (followers.c.followed_id == Post.author_id)).filter(
                followers.c.follower_id == self.id).order_by(
                    Post.timestamp.desc())
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(3000))
    img = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship("User", backref="books")
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship("Genre", backref="Posts")

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class RevokedTokenModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)
    
    def __repr__(self):
        return '<Token {}>'.format(self.body)
    
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))

    def __repr__(self):
        return '<Genre {}>'.format(self.body)
    

class GenreSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Genre
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    avatar = ma.auto_field()

class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post
        load_instance = True

    id = auto_field()
    title = auto_field()
    body = auto_field()  
    img = auto_field() 

    genre = fields.Nested(GenreSchema)
    author = fields.Nested(UserSchema) 

    