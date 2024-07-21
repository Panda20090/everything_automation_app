from plyer import notification
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Data Automation App',
        timeout=10
    )

def send_email(subject, body, to_email):
    from_email = "pagestowages@gmail.com"
    from_password = "nsxm wnrm nvcq gamm"

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

def generate_report(data_file, output_file):
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    report = f"Report for {data_file}:\n\n"
    for key, value in data.items():
        report += f"{key}: {value}\n"
    
    with open(output_file, 'w') as f:
        f.write(report)
    
    return report

