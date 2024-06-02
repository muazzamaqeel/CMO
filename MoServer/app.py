import os
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import logging
import traceback
from flask import Flask, send_from_directory, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='assets', template_folder='.')
CORS(app)
logger = logging.getLogger('email_automation')
logging.basicConfig(level=logging.DEBUG)

def send_emails(csv_file_path, template_file_path, sender_email, sender_password):
    try:
        # Read the CSV file
        contacts = pd.read_csv(csv_file_path)

        # Read the email template
        with open(template_file_path, 'r') as file:
            email_template = file.read()

        # Set up the SMTP server for Outlook
        smtp_server = 'smtp.office365.com'
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        for index, row in contacts.iterrows():
            recipient_email = row['Email']
            recipient_name = row['Name']
            personalized_email = email_template.replace('NAME', recipient_name)

            # Create a multipart message and set headers
            msg = MIMEMultipart("alternative")
            msg['Subject'] = 'Introducing Our New Product'
            msg['From'] = sender_email
            msg['To'] = recipient_email

            # Add plain text and HTML parts
            part1 = MIMEText(personalized_email, "plain")
            part2 = MIMEText(personalized_email, "html")

            # Attach parts into message container
            msg.attach(part1)
            msg.attach(part2)

            server.sendmail(sender_email, recipient_email, msg.as_string())
            logger.info(f"Email sent to {recipient_email}")

        server.quit()
        return True, "Emails sent successfully!"
    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"Failed to send emails: {e}")
        return False, "Authentication failed. Please check your email and password."
    except Exception as e:
        logger.error(f"Failed to send emails: {e}")
        logger.error(traceback.format_exc())
        return False, "An error occurred while sending emails. Please try again later."

@app.route('/send_emails', methods=['POST'])
def handle_send_emails():
    try:
        # Ensure the uploads directory exists
        if not os.path.exists('uploads'):
            os.makedirs('uploads')

        csv_file = request.files['csvFile']
        email_template_file = request.files['emailTemplate']
        sender_email = request.form['senderEmail']
        sender_password = request.form['senderPassword']

        csv_file_path = os.path.join('uploads', csv_file.filename)
        email_template_file_path = os.path.join('uploads', email_template_file.filename)

        logger.debug(f"Saving CSV file to {csv_file_path}")
        logger.debug(f"Saving email template file to {email_template_file_path}")

        csv_file.save(csv_file_path)
        email_template_file.save(email_template_file_path)

        success, message = send_emails(csv_file_path, email_template_file_path, sender_email, sender_password)
        return jsonify({'success': success, 'message': message})

    except Exception as e:
        logger.error(f"Exception in /send_emails: {e}")
        return jsonify({'success': False, 'message': str(e)})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static_files(filename):
    if filename.startswith('assets/'):
        return send_from_directory('assets', filename[len('assets/'):])
    elif filename.startswith('forms/'):
        return send_from_directory('forms', filename[len('forms/'):])
    else:
        return render_template(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
