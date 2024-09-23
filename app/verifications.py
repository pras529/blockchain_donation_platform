from app.models import Project, Notification

def verify_project_milestone(project_id, verification_data):
    project = Project.query.get(project_id)
    if project and verification_data == project.verification_data:
        project.verified = True
        notify_donors(project_id, f"Milestone for {project.name} verified!")
        return True
    return False
