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
    for i in range(5):
        #Incident, date, location, offender, command, rank, age, race, gender, victim
        incidents = ["DOMESTIC ABUSE", "RACE DISCRIMINATION", "GENDER DISCRIMINATION", "SEXUAL ASSAULT", "VEHICULAR ACCIDENT"]
        commands = ["New York Yankees", "San Antonio Spurs", "Dallas Cowboys", "University of Texas Longhorns"]
        genders = ["MALE", "FEMALE"]
        races = ["WITHHELD", "OTHER", "CAUCASIAN", "AFRICAN-AMERICAN", "ASIAN"]
        persons = ["E-1", "E-2", "E-3", "E-4", "E-5", "E-6", "E-7", "E-8", "E-9", "O-1", "O-2", "O-3", "O-3", "O-4", "O-5", "O-6", "O-7", "O-8", "O-9", "CIV"]
        adeo = ["YES", "NO"]
        num = ["ONE", "TWO"]
        
        # Generate the random data for each choice
        d = datetime.now()
        incident = random.choices(incidents)[0]
        command = random.choices(commands)[0]
        person = random.choices(persons)[0]
        gender = random.choices(genders)[0]
        race = random.choices(races)[0]
        alc = random.choices(adeo)[0]
        drugs = random.choices(adeo)[0]
        person2 = random.choices(persons)[0]
        gender2 = random.choices(genders)[0]
        race2 = random.choices(races)[0]
        command2 = random.choices(commands)[0]
        num = random.choices(num)[0]
        # Build the message from that data\
        message = """RTTUZYUW RHOIAAA0001 1451706-UUUU--RHSSSUU.
        ZNR UUUUU
        R 251651Z MAY 11 MID200000886340U
        FM NAVTALACQGRU PACIFIC NORTHWEST SEATTLE WA
        TO COMNAVCRUITREG WEST MILLINGTON TN
        COMNAVCRUITCOM MILLINGTON TN
        NETC PENSACOLA FL
        CNO WASHINGTON DC
        INFO COMUSFLTFORCOM NORFOLK VA
        CHINFO WASHINGTON DC
        NAVY JAG WASHINGTON DC
        COMNAVPERSCOM MILLINGTON TN
        CNIC WASHINGTON DC
        DIRNAVCRIMINVSERV QUANTICO VA
        COMNAVREG NW SILVERDALE WA
        NAVCRIMINVSERVRA BREMERTON WA
        NAVCRIMINVSERVRA EVERETT WA
        NAVTALACQGRU PACIFIC NORTHWEST SEATTLE WA
        BT
        UNCLAS
        SECINFO/U/-//
        MSGID/OPREP-3NUS,USMTF,2011/NAVTALACQGRU PACIFIC NORTHWEST SEATTLE
        WA/002//
        FLAGWORD/NAVY UNIT SITREP/-//
        TIMELOC/211502MAY2011/SEATTLE WA/FINAL//
        GENTEXT/INCIDENT IDENTIFICATION AND DETAILS//\n
        """
        if num == "ONE":
            message += f"1. INCIDENT: {incident}\n2. DATE OF INCIDENT: {d}\n3. LOCATION OF INCIDENT: {command}\n4. OFFENDER: {person}\n5. COMMAND: {command}\n6. GENDER: {gender}\n7. AGE: {random.randrange(18, 55)}\n8. RACE: {race}\n9. ALCOHOL: {alc}, DRUGS: {drugs}\n10. SUMMARY/BRIEF DESCRIPTION OF INCIDENT: Incident occured on {d} at {command} with {person}"
        else:
            message += f"1. INCIDENT: {incident}\n2. DATE OF INCIDENT: {d}\n3. LOCATION OF INCIDENT: {command}\n4. OFFENDER: {person}\n5. COMMAND: {command}\n6. GENDER: {gender}\n7. AGE: {random.randrange(18, 55)}\n8. RACE: {race}\n9. VICTIM: {person2}\n10. GENDER OF VICTIM: {gender2}\n11. AGE OF VICTIM: {random.randrange(18, 55)}\n12. RACE OF VICTIM: {race2}\n13. ALCOHOL: {alc}, DRUGS: {drugs}\n14. SUMMARY/BRIEF DESCRIPTION OF INCIDENT: Incident occured on {d} at {command} with {person}"
        # Send message and loop
        send_email("sitreceiver@outlook.com", "sitrep", message, "")
        time.sleep(1)