import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import random
from datetime import datetime
import time

def send_email(email_recipient,
               email_subject,
               email_message,
               attachment_location = ''):

    email_sender = 'sitcreator@outlook.com'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message, 'plain'))

    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login('sitcreator@outlook.com', 'sitrepdummyemail062021')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True

if __name__ == "__main__":
    for i in range(25):
        #Incident, date, location, offender, command, rank, age, race, gender, victim
        incident = ["DOMESTIC ABUSE", "RACE DISCRIMINATION", "GENDER DISCRIMINATION", "SEXUAL ASSAULT", "VEHICULAR ACCIDENT"]
        commands = ["New York Yankees", "San Antonio Spurs", "Dallas Cowboys", "University of Texas Longhorns"]
        gender = ["MALE", "FEMALE"]
        race = ["WITHHELD", "OTHER", "CAUCASIAN", "AFRICAN-AMERICAN", "ASIAN"]
        person = ["E-1", "E-2", "E-3", "E-4", "E-5", "E-6", "E-7", "E-8", "E-9", "O-1", "O-2", "O-3", "O-3", "O-4", "O-5", "O-6", "O-7", "O-8", "O-9", "CIV"]
        adeo = ["YES", "NO"]
        d = datetime.now()
        message = f"1. INCIDENT: {random.choices(incident)[0]}\n2. DATE OF INCIDENT: {d}\n3. LOCATION OF INCIDENT: {random.choices(commands)[0]}\n4. OFFENDER: {random.choices(person)[0]}\n5. COMMAND: {random.choices(commands)[0]}\n6. GENDER: {random.choices(gender)[0]}\n7. AGE: {random.randrange(18, 55)}\n8. RACE: {random.choices(race)[0]}\n9. ALOCOHOL: {random.choices(adeo)[0]}, DRUGS: {random.choices(adeo)[0]}"
        send_email("sitreceiver@outlook.com", "sitrep", message, "")
        time.sleep(5)