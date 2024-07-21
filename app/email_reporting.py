import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def send_report():
    with open('data/performance_report.txt', 'r') as file:
        report = file.read()

    subject = "Performance Report"
    body = f"Please find the attached performance report.\n\n{report}"
    to_email = "pagestowages@gmail.com"
    send_email(subject, body, to_email)

def send_email(subject, body, to_email):
    from_email = "pagestowages@gmail.com"
    from_password = "wtzc dqkv ojvv pqrb"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
