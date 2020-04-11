# Send an email
# python send_an_email.py


import smtplib


def send_email(receiver_email_address, subject, body):
    '''
    Send email

    Arguments:
        receiver_email_address (str): receiver
        subject (str): email subject
        body (str): email body

    Returns
        None
    '''
    message = 'Subject : {}\n\n{}'.format(subject, body)
    sender_email_address = 'sender_email_address@gmail.com' 
    sender_email_password = 'sender_email_address_password' 

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email_address, sender_email_password)
        server.sendmail(sender_email_address, receiver_email_address, message)


if __name__ == '__main__':
    send_email('receiver_email_address@gmail.com', 'Test email', 'This is a test email. Cheers')
