from .models import Charity, Project
from . import db

def create_project(charity_id, name, description):
    new_project = Project(charity_id=charity_id, name=name, description=description)
    db.session.add(new_project)
    db.session.commit()

def verify_milestone(project_id, verification_data):
    project = Project.query.get(project_id)
    project.verified = True
    project.verification_data = verification_data
    db.session.commit()
