import smtplib  # for creating smtp server, Python provides smtplib module
from email.message import EmailMessage
from string import Template  #built-in lib
from pathlib import Path  # similar to os.path



def send_custom_email(receiver):
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Andrei Neagoie'
    email['to'] = 'ed828dev@gmail.com'
    email['subject'] = 'You won 1,000,000 dollars!'

    email.set_content(html.substitute({'name': receiver}), 'html')  # html format

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()  # hello message
        smtp.starttls()  # encryption
        smtp.login('ed828python@gmail.com', 'tomisadog')
        # need to set Less secure app access of the account to ON
        smtp.send_message(email)
        print('all good boss!')


if __name__ == '__main__':
    send_custom_email("Edward")
