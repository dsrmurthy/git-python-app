import smtplib   #pip install smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server details
smtp_server = 'smtp.gmail.com'  # Example: Gmail's SMTP server
smtp_port = 587  # Port for TLS (587) or 465 (SSL)

# Sender email and password
sender_email = 'your_email@gmail.com'
sender_password = 'your_email_password'

# Recipient email
recipient_email = 'recipient_email@example.com'

# Create the message
subject = "Test Email from Python"
body = "This is a test email sent using Python and SMTP protocol."

# Create the MIME object to structure the email
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject

# Attach the email body to the message
message.attach(MIMEText(body, 'plain'))

try:
    # Set up the SMTP server and login
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection using TLS
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email. Error: {e}")

finally:
    # Close the connection to the SMTP server
    server.quit()
