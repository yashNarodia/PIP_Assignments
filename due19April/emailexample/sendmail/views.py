import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import get_template,render_to_string
from django.core.mail import send_mail,EmailMessage,send_mass_mail
# Create your views here.

def email_with_attachment(request,*args,**kwargs):

    subject = 'This is email subject'
    
    ctx = {
        'username' : 'Alen1234',
        'first_name':'Alen',
        'last_name':'Jake',
    }
    
    msg = render_to_string('test_email/simple_email.html',ctx)
    
    from_email = 'fromemail@example.com'
    
    to_email = ['toemail@example.com']

    mail = EmailMessage(
        subject,
        msg,
        from_email,
        to_email,
    )
    
    mail.content_subtype='html'

    mail.attach_file(file_path)
    
    email_res = mail.send()
    
    return HttpResponse(email_res)
    