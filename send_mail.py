import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smpt_server = 'smtp.mailtrap.io'
    login = '00b1248e9e884c'
    password = '3dbd513d3dd7bd'
    message = f"<h3> New Feedback Submission</h3><ul><li>{customer}</li><li>{dealer}</li><li>{rating}</li><li>{comments}</li></ul>"
    sender_email = 'email@example.com'
    receiver_email = 'email2@example.com'
    msg= MIMEText(message, 'html')
    msg['Subject'] =  'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    #Send Email
    with smtplib.SMTP(smpt_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())