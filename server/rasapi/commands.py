"""
commands.py
- provides a command line utility for interacting with the
  application to perform interactive debugging and setup
"""

import click

from flask import Blueprint
from rasapi.models import db, Resource, Reservation


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
        {'rsrc_name': 'PSCM-Bench-SPA2-PDS', 'department': 'Vehicle Platform', 'status': 'active', 'ci_level': 'component', 'responsible_user': 'Deng, Yibo', 'location': 'CIC', 'description': '', 'rsrc_type': 'Bench'},
        {'rsrc_name': 'MiniHIL-HIL-SPA2-PDS', 'department': 'Vehicle Platform', 'status': 'active', 'ci_level': 'component', 'responsible_user': 'Cheng, yuxin', 'location': 'CIC', 'description': '', 'rsrc_type': 'HIL'},
        {'rsrc_name': 'VCUapp-HIL-SPA2-PDS', 'department': 'Software& Electronic Platform', 'status': 'active', 'ci_level': 'system', 'responsible_user': 'Magnus', 'location': 'CIC', 'description': '', 'rsrc_type': 'HIL'},
        {'rsrc_name': 'Boxcar620C/MP1-Boxcar-SPA2-PDS', 'department': 'Software& Electronic Platform', 'status': 'removed', 'ci_level': 'system', 'responsible_user': 'Zhu, Rong', 'location': 'CIC', 'description': '620C/MP1', 'rsrc_type': 'Boxcar'},
        {'rsrc_name': 'ITA-HILs-HIL-ICUP-PDS', 'department': 'Connected Experience', 'status': 'maintenance', 'ci_level': 'domain', 'responsible_user': 'Wang, jinyan', 'location': 'CIC', 'description': '', 'rsrc_type': 'HIL'},
    ]

    for r in resources:
        resource = Resource(rsrc_name=r['rsrc_name'], department=r['department'], status=r['status'], ci_level=r['ci_level'], responsible_user=r['responsible_user'], location=r['location'], description=r['description'], rsrc_type=r['rsrc_type'])
        db.session.add(resource)

    db.session.commit()
    click.echo('Done.')

