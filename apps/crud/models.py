from datetime import datetime

from apps.app import db
#from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    # テーブル名を指定する
    __tablename__ = "users"
    # カラムを定義する
    id = db.Column(db.Integer, primary_key=True)
    musicname = db.Column(db.String, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


