"""
commands.py
- provides a command line utility for interacting with the
  application to perform interactive debugging and setup
"""

import click

from flask import Blueprint
from rasapi.models import db, Resource


cmd = Blueprint('cmd', __name__)


@cmd.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@cmd.cli.command()
def forgersrc():
    """Generate fake data."""
    db.create_all()

    resources = [
        {'rsrc_name': 'ad-adlab-hil-1', 'department': 'dept', 'status': 'active', 'ci_level': 'component', 'responsible_user': '1', 'location': 'CIC', 'description': 'AD Lab Vector HIL rig for VCU1 and AD sensors', 'rsrc_type': 'HIL'},
        {'rsrc_name': 'adas-component-hil', 'department': 'dept', 'status': 'active', 'ci_level': 'component', 'responsible_user': '1', 'location': 'CIC', 'description': 'asdm flc2 flr production rig', 'rsrc_type': 'HIL'},
        {'rsrc_name': 'eh-icup-1', 'department': 'dept', 'status': 'active', 'ci_level': 'component', 'responsible_user': '1', 'location': 'CIC', 'description': 'used for EH 522A and 622A project test', 'rsrc_type': 'Boxcar'},
        {'rsrc_name': 'adas-domian-hil-argus2-pds-1', 'department': 'dept', 'status': 'removed', 'ci_level': 'component', 'responsible_user': '1', 'location': 'CIC', 'description': 'PDS ADAS HIL rig', 'rsrc_type': 'HIL'},
        {'rsrc_name': 'steer-component-pscm-cma-pds-2', 'department': 'dept', 'status': 'maintenance', 'ci_level': 'component', 'responsible_user': '1', 'location': 'CIC', 'description': 'PDS steer bench', 'rsrc_type': 'Test bench'},
    ]

    for r in resources:
        resource = Resource(rsrc_name=r['rsrc_name'], department=r['department'], status=r['status'], ci_level=r['ci_level'], responsible_user=r['responsible_user'], location=r['location'], description=r['description'], rsrc_type=r['rsrc_type'])
        db.session.add(resource)

    db.session.commit()
    click.echo('Done.')

