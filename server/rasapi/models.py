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
    resources = db.relationship('Resource', backref="user", lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    email=self.email,
                    cdsid=self.cdsid,
                    password_hash=self.password_hash,
                    username=self.username,
                    user_type=self.user_type,
                    resources=[resource.to_dict() for resource in self.resources])


class Resource(db.Model):
    __tablenmae__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    rsrc_name = db.Column(db.String(50))
    department = db.Column(db.String(50))
    status = db.Column(db.String(20))
    ci_level = db.Column(db.String(20))
    responsible_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    location = db.Column(db.String(255))
    description = db.Column(db.String(255))
    rsrc_type = db.Column(db.String(20))

    def to_dict(self):
        return dict(id=self.id,
                    rsrc_name=self.rsrc_name,
                    department=self.department,
                    status=self.status,
                    ci_level=self.ci_level,
                    responsible_user=self.responsible_user,
                    location=self.location,
                    description=self.description,
                    rsrc_type=self.rsrc_type)


class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    booked_rsrc_name = db.Column(db.String(50))
    booked_rsrc_id = db.Column(db.Integer)
    booked_for_name = db.Column(db.String(50))
    booked_by_name =db.Column(db.String(50))
    booked_from = db.Column(db.String(50))
    booked_until = db.Column(db.String(50))
    description = db.Column(db.String(255))

    def to_dict(self):
        return dict(id=self.id,
                    booked_rsrc_name=self.booked_rsrc_name,
                    booked_rsrc_id=self.booked_rsrc_id,
                    booked_for_name=self.booked_for_name,
                    booked_by_name=self.booked_by_name,
                    booked_from=self.booked_from,
                    booked_until=self.booked_until,
                    description=self.description)
