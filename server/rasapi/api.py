"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Resource, Reservation


api = Blueprint('api', __name__)


@api.route('/hello/<string:name>/')
def say_hello(name):
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)


@api.route('/resources/', methods=('GET','POST'))
def get_add_resources():
    if request.method == 'GET':
        resources = Resource.query.all()
        return jsonify({'resources': [r.to_dict() for r in resources]})
    elif request.method == 'POST':
        data = request.get_json()
        resource = Resource(rsrc_name=data['rsrc_name'], department=data['department'], ci_level=data['ci_level'], responsible_user=data['responsible_user'], location=data['location'], status=data['status'], description=data['description'], rsrc_type=data['rsrc_type'])
        db.session.add(resource)
        db.session.commit()
        return jsonify(resource.to_dict()), 201


@api.route('/resources/<int:id>/', methods=('GET', 'PUT'))
def get_update_resource(id):
    resource = Resource.query.get(id)
    
    if request.method == 'GET':
        return jsonify({'resource': resource.to_dict()})

    elif request.method == 'PUT':
        data = request.get_json()

        rsrc_name = data['rsrc_name']
        department=data['department']
        ci_level=data['ci_level']
        responsible_user=data['responsible_user']
        location=data['location']
        status = data['status']
        description = data['description']
        rsrc_type = data['rsrc_type']

        resource.rsrc_name = rsrc_name
        resource.department = department
        resource.ci_level = ci_level
        resource.responsible_user = responsible_user
        resource.location = location
        resource.status = status
        resource.description = description
        resource.rsrc_type = rsrc_type

        db.session.commit()
        return jsonify(resource.to_dict()), 201



@api.route('/resources/<int:id>/', methods=["DELETE"])
def delete_resource(id):
    resource = Resource.query.get_or_404(id)
    db.session.delete(resource)
    db.session.commit()
    return "Deleted"


@api.route('/reservations/', methods=('GET','POST'))
def get_add_reservations():
    if request.method == 'GET':
        reservations = Reservation.query.all()
        return jsonify({'reservations': [rs.to_dict() for rs in reservations]})
    elif request.method == 'POST':
        data = request.get_json()
        reservation = Reservation(booked_rsrc_name=data['booked_rsrc_name'], booked_for_name=data['booked_for_name'], booked_by_name=data['booked_by_name'], booked_from=data['booked_from'], booked_until=data['booked_until'], description=data['description'])
        db.session.add(reservation)
        db.session.commit()
        return jsonify(reservation.to_dict()), 201


@api.route('/reservations/<int:id>/', methods=('GET', 'PUT'))
def get_update_reservation(id):
    reservation = Reservation.query.get(id)
    
    if request.method == 'GET':
        return jsonify({'reservation': reservation.to_dict()})

    elif request.method == 'PUT':
        data = request.get_json()

        booked_rsrc_name = data['booked_rsrc_name']
        booked_for_name = data['booked_for_name']
        booked_by_name = data['booked_by_name']
        booked_from = data['booked_from']
        booked_until = data['booked_until']
        description = data['description']

        reservation.booked_rsrc_name = booked_rsrc_name
        reservation.booked_for_name = booked_for_name
        reservation.booked_by_name = booked_by_name
        reservation.booked_from = booked_from
        reservation.booked_until = booked_until
        reservation.description = description

        db.session.commit()
        return jsonify(reservation.to_dict()), 201


@api.route('/reservations/<int:id>/', methods=["DELETE"])
def delete_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    db.session.delete(reservation)
    db.session.commit()
    return "Deleted"
