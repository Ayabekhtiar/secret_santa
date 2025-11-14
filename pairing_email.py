import smtplib # library to deliver the email
from email.message import EmailMessage # library to construct the email
import random # library to do random operations


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



# constraints for people who shouldn't get paired for safety reasons
constraints = {
    'Taha': ['Sarah'],
    'Sarah': ['Taha']
}



# secret santa pairing function
def generate_pairs(recipients, constraints, max_tries=100):
    names = list(recipients.keys())

    # loop
    for _ in range(max_tries):
        receivers = names.copy()
        random.shuffle(receivers) # if we don't shuffle, everyone will get themselves as secret santas
        pairs = dict(zip(names, receivers)) # creating a dictionary with the secret santa pairs

        # checking that veryone gives and receives exactly once
        if len(set(pairs.keys())) != len(names):
            continue
        if len(set(pairs.values())) != len(names):
            continue

        # checking constraints: no self and no forbidden pairs
        valid = True
        for giver, receiver in pairs.items():
            if giver == receiver:
                valid = False
                break # stops the inner loop, not the whole function unless the max tries number is reached
            if receiver in constraints.get(giver, []): # if the giver exists in constraints, this returns their associated list; otherwise it returns []
                valid = False
                break 

        if valid:
            return pairs

    raise ValueError("Unable to find a valid Secret Santa assignment with these constraints.")


pairs = generate_pairs(recipients, constraints)


# counters to check if all emails were sent
sent_success = 0
sent_fail = 0

# loop to tell everyone their assigned person using the send_email function
for name, email in recipients.items():
    assigned_person = pairs[name]  

    body = f"""
Hello my little Christmas elf {name},

You are the Secret Santa of: {assigned_person}.
Thank you for participating 🎄
"""
    # assertion check using the counter variables
    try:
        send_mail(email, "Secret Santa reveal 🎅", body)
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
