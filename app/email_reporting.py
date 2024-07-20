import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def send_summary_email(subject, body, to_email):
    from_email = "your_email@example.com"
    from_password = "your_email_password"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def generate_summary_report():
    summary = {
        "Google Trends Analysis": "Average value: 123",
        "Twitter Analysis": "Keyword count: 456"
    }
    return summary

def prepare_email_body(summary):
    body = "Summary Report:\n\n"
    for key, value in summary.items():
        body += f"{key}: {value}\n"
    return body

def send_report():
    summary = generate_summary_report()
    body = prepare_email_body(summary)
    send_summary_email("Daily Summary Report", body, "recipient@example.com")
