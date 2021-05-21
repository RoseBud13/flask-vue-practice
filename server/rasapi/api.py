"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Resource


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
        resource = Resource(rsrc_name=data['rsrc_name'], status=data['status'], description=data['description'], rsrc_type=data['rsrc_type'])
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
        status = data['status']
        description = data['description']
        rsrc_type = data['rsrc_type']

        resource.rsrc_name = rsrc_name
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
