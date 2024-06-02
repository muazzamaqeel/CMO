import pandas as pd
import smtplib
from email.mime.text import MIMEText

def send_emails(csv_file_path, template_file_path, sender_email, sender_password):
    try:
        # Read the CSV file
        contacts = pd.read_csv(csv_file_path)

        # Read the email template
        with open(template_file_path, 'r') as file:
            email_template = file.read()

        # Set up the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        for index, row in contacts.iterrows():
            recipient_email = row['Email']
            recipient_name = row['Name']
            personalized_email = email_template.replace('NAME', recipient_name)

            msg = MIMEText(personalized_email)
            msg['Subject'] = 'Introducing Our New Product'
            msg['From'] = sender_email
            msg['To'] = recipient_email

            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email}")

        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send emails: {e}")
        return False
