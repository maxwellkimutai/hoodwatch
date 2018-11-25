from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_amber_email(title,content,receiver):
    # Creating message subject and sender
    subject = 'Amber Alert'
    sender = 'Hood Watch'

    #passing in the context vairables
    text_content = render_to_string('email/amberemail.txt',{"title": title,"content":content})
    html_content = render_to_string('email/amberemail.html',{"title": title,"content":content})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
