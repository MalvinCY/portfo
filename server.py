from flask import Flask, render_template, redirect, url_for, request
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Email configuration — set these as environment variables on PythonAnywhere
NOTIFY_EMAIL = "mcysiew@ymail.com"
SMTP_USER = os.environ.get("SMTP_USER", "mcysiew@ymail.com")
SMTP_PASS = os.environ.get("SMTP_PASS", "")  # Set via environment variable on PythonAnywhere

@app.route("/")
def my_home():
    return render_template('index.html')



@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
    

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


def send_notification_email(data):
    """Send an email notification when someone submits the contact form."""
    if not SMTP_PASS:
        print("SMTP_PASS not set — skipping email notification.")
        return

    try:
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = NOTIFY_EMAIL
        msg["Subject"] = f"Portfolio Contact: {data.get('subject', 'No subject')}"

        body = (
            f"New message from your portfolio contact form:\n\n"
            f"From: {data.get('email', 'Unknown')}\n"
            f"Subject: {data.get('subject', 'No subject')}\n\n"
            f"Message:\n{data.get('message', '')}\n"
        )
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        print("Notification email sent successfully.")
    except Exception as e:
        print(f"Failed to send notification email: {e}")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        send_notification_email(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'