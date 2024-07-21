import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def notify(subject, body):
    print(f"Notification: {subject}\n{body}")

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

def generate_report(data_file, output_file):
    with open(data_file, 'r') as file:
        data = file.read()
    with open(output_file, 'w') as file:
        file.write(data)
    return data
