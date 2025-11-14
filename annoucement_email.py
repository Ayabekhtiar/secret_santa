import smtplib # library to deliver the email
from email.message import EmailMessage # library to construct the email

# setting up the relevant variables to send emails
SMTP_SERVER = "smtp.gmail.com" # stmp server to connect to for gmail
SMTP_PORT = 587 # port for sending emails
USERNAME = "your_gmail_adress" # change to your gmail adress
PASSWORD = "app_password" # NOT YOUR EMAIL PASSWORD, it is the app password that you can generate after activating 2-step verification in your gmail security parameters

# function to send emails
def send_mail(to, subject, body): 
    msg = EmailMessage() # empty email draft 
    # we have to write "From", "To", "Subject" like this for Gmail to recognize the labels
    msg["From"] = USERNAME
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body) # the body is the email message just in case

    # block to connect to server and send email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.send_message(msg)


# for the dictionary, set up the keys with names as you want them to be written in the emails
recipients = {'Aya': 'aya@gmail.com', 
'Taha': 'taha@gmail.com', 
'Sarah': 'sarah@gmail.com', 
'Naima': 'naima@gmail.com'}

# counters to check if all emails were sent
sent_success = 0
sent_fail = 0

# loop to send emails to everyone using the send_email function
for name, email in recipients.items():
    body = f"""Hello my little Christmas elf {name},

This is your personalized Secret Santa message! Please let me know if you want to participate.

Wishing you a wonderful Christmas season 🎄
"""
    # assertion check using the counter variables
    try:
        send_mail(email, "Secret Santa 🎅", body) # object title in the middle
        print(f"✔ Email successfully sent to {name} ({email})") 
        sent_success += 1

    except Exception as e:
        print(f"❌ Failed to send email to {name} ({email})")
        print(f"   Error: {e}")
        sent_fail += 1

# counter results
print("\n====== SUMMARY ======")
print(f"Emails sent successfully: {sent_success}")
print(f"Emails failed: {sent_fail}")
