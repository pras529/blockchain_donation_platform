import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app
import logging

class NotificationService:
    def __init__(self):
        self.smtp_server = current_app.config['EMAIL']['smtp_server']
        self.smtp_port = current_app.config['EMAIL']['smtp_port']
        self.email_address = current_app.config['EMAIL']['email_address']
        self.email_password = current_app.config['EMAIL']['email_password']

    def send_email(self, recipient_email, subject, message):
        try:
            # Set up the MIME
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the message body
            msg.attach(MIMEText(message, 'plain'))

            # Set up the SMTP server connection
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Enable security
                server.login(self.email_address, self.email_password)

                # Send the email
                server.sendmail(self.email_address, recipient_email, msg.as_string())
                logging.info(f"Email sent to {recipient_email} with subject '{subject}'")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {str(e)}")

    def send_donation_confirmation(self, donor_email, project_name, amount):
        subject = "Donation Confirmation"
        message = f"Dear Donor,\n\nThank you for your generous donation of ${amount} to the project '{project_name}'.\n\n" \
                  f"We appreciate your support in making a difference.\n\nBest regards,\nBlockchain Donation Platform"
        self.send_email(donor_email, subject, message)

    def send_milestone_achievement(self, donor_email, project_name, milestone):
        subject = "Milestone Achieved"
        message = f"Dear Donor,\n\nWe are excited to inform you that the project '{project_name}' has successfully achieved the milestone: {milestone}.\n\n" \
                  f"Thank you for your continued support.\n\nBest regards,\nBlockchain Donation Platform"
        self.send_email(donor_email, subject, message)

    def send_project_update(self, donor_email, project_name, update_message):
        subject = f"Update on '{project_name}'"
        message = f"Dear Donor,\n\nHere's the latest update on the project '{project_name}':\n\n{update_message}\n\n" \
                  f"Thank you for being a part of this journey.\n\nBest regards,\nBlockchain Donation Platform"
        self.send_email(donor_email, subject, message)

    def notify_charity_project_submission(self, charity_email, project_name):
        subject = "Project Submission Confirmation"
        message = f"Dear Charity,\n\nYour project '{project_name}' has been successfully submitted to the Blockchain Donation Platform for review.\n\n" \
                  f"We will notify you once the project goes live.\n\nBest regards,\nBlockchain Donation Platform"
        self.send_email(charity_email, subject, message)
