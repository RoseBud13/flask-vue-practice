"""
models.py
- Data classes for the rasapi application
"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    cdsid = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(128))
    username = db.Column(db.String(50))
    user_type = db.Column(db.String(20))

    def to_dict(self):
        return dict(id=self.id,
                    email=self.email,
                    cdsid=self.cdsid,
                    password_hash=self.password_hash,
                    username=self.username,
                    user_type=self.user_type)


class Resource(db.Model):
    __tablenmae__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    rsrc_name = db.Column(db.String(50))
    status = db.Column(db.String(20))
    description = db.Column(db.String(255))
    rsrc_type = db.Column(db.String(20))

    def to_dict(self):
        return dict(id=self.id,
                    rsrc_name=self.rsrc_name,
                    status=self.status,
                    description=self.description,
                    rsrc_type=self.rsrc_type)
