import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def new_meeting(toaddr, id, pw):
    #Code from http://naelshiab.com/tutorial-send-email-python/

    fromaddr = "isaacglance@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "You created a meeting with Doogle"

    body = "Meeting name: {}\nMeeting password: {}\n\n" \
           "Next, send invites and set meeting time parameters".format(id, pw)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "BigColor914!")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return

def invite_group(addr_list, id, organizer_email): #No code needed, they will be required by google to sign into the correct address
    fromaddr = "isaacglance@gmail.com"
    msg = MIMEMultipart()
    # The to-address can actually be a list of to-addresses.
    msg['From'] = fromaddr
    msg['To'] = "New User"
    #
    msg['Subject'] = "You have been invited to a meeting with Doogle"
    body = "You have been invited to a meeting by {}!\nMeeting name: \"{}\"  (use this to log in)\n\n" \
           "Please log in with the meeting name and your email address. " \
           "You will be prompted to log in with your google account.".format(organizer_email, id)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "BigColor914!")
    text = msg.as_string()
    server.sendmail(fromaddr, addr_list, text)
    server.quit()
    return