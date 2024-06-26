import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = 'smtp-mail.outlook.com'
PORT = 587

From_email = 'agneljosy1@outlook.com'
To_email = 'agneljosy@gmail.com'
Password = 'Agnel@1234'

# HTML email content
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
        body {
            margin: 0;
            padding: 0;
            width: 100%;
            font-family: Lato, sans-serif;
            font-size: 18px;
            background-color: #F5F8FA;
        }
        #email {
            margin: auto;
            width: 100%;
            max-width: 600px;
            background-color: #ffffff;
        }
        .header {
            background-color: #00A4BD;
            text-align: center;
            padding: 20px;
            color: #ffffff;
        }
        .content {
            padding: 30px;
        }
        h1 {
            font-size: 56px;
            margin: 0;
        }
        h2 {
            font-size: 28px;
            font-weight: 900;
            margin: 0 0 10px;
        }
        p {
            font-weight: 100;
            color:black;
            margin: 0 0 15px;
        }
        .button {
            background-color: #00A4BD;
            color: #ffffff;
            padding: 15px 25px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            margin-top: 20px;
        }
        @media screen and (max-width: 600px) {
            .content {
                padding: 20px;
            }
            h1 {
                font-size: 32px;
            }
            h2 {
                font-size: 24px;
            }
        }
    </style>
</head>
<body>
    <div id="email">
        <div class="header">
            <h1>Welcome!</h1>
        </div>
        <div class="content">
            <h2>Welcome to WhatsApp Reminder Assistant!</h2>
            <p>
                Hello [Customer Name],
            </p>
            <p>
                Thank you for signing up for WhatsApp Reminder Assistant. We are thrilled to have you on board!
            </p>
            <p>
                Our service will help you stay organized and never miss an important task or event again. With WhatsApp Reminder Assistant, you can easily set reminders and get notified directly on your WhatsApp.
            </p>
            <p>
                Click the button below to start exploring our features and set your first reminder.
            </p>
            <p style="text-align: center;">
                <a href="{% url 'login' %}" class="button">Get Started</a>
            </p>
            <p>
                If you have any questions, feel free to reach out to our support team.
            </p>
            <p>
                Best regards,<br>
                The WhatsApp Reminder Assistant Team
            </p>
        </div>
    </div>
</body>
</html>

'''

# Create a MIMEMultipart object
msg = MIMEMultipart('alternative')
msg['Subject'] = "Welcome to WhatsApp Reminder Assistant!"
msg['From'] = From_email
msg['To'] = To_email

# Attach the HTML content to the MIMEMultipart object
html_part = MIMEText(html_content, 'html')
msg.attach(html_part)

try:
    smtp = smtplib.SMTP(HOST, PORT)
    status_code, response = smtp.starttls()
    print(f'[*] Starting TLS connection: {status_code} {response}')

    status_code, response = smtp.login(From_email, Password)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(From_email, To_email, msg.as_string())
    print("[*] Email sent successfully!")
except Exception as e:
    print(f"[*] Error sending email: {e}")
finally:
    smtp.quit()
