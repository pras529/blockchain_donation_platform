from app.models import Donation, Project, Notification
from app.blockchain import get_transaction_receipt
from flask_socketio import emit

def track_donations(project_id):
    donations = Donation.query.filter_by(project_id=project_id).all()
    total_donated = sum([donation.amount for donation in donations])
    emit('donation_update', {'project_id': project_id, 'total_donated': total_donated})
    return total_donated

def notify_donors(project_id, milestone_message):
    donors = Donation.query.filter_by(project_id=project_id).all()
    for donor in donors:
        notification = Notification(user_id=donor.user_id, message=milestone_message)
        notification.save()
        # Optionally, trigger an email or SMS to the donor
