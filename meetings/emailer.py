import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def new_meeting(toaddr, id, pw):
    #Code from http://naelshiab.com/tutorial-send-email-python/

    fromaddr = "isaacglance@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "You created a meeting with Doogle"

    body = "Meeting name: {}/nMeeting password: {}/n/n" \
           "Next, send invites and set meeting time parameters".format(id, pw)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "BigColor914!")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return

def invite_group(addr_list, id, code): #TODO: RANDOMLY GENERATE CODE
    fromaddr = "isaacglance@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "You have been invited to a meeting with Doogle"

    body = "Meeting name: {}/nYour meeting code (use this to log in): {}/n/n" \
           "Please log in with the meeting name and your unique code".format(id, code)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "BigColor914!")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return