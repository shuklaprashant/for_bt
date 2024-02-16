import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, body):
        try:
            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            # Create SMTP session for sending the mail
            session = smtplib.SMTP(self.smtp_server, self.smtp_port)
            session.starttls()  # Enable encryption
            session.login(self.sender_email, self.sender_password)  # Login
            text = message.as_string()
            session.sendmail(self.sender_email, receiver_email, text)
            session.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")
