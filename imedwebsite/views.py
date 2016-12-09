from django.shortcuts import render
from django.shortcuts import redirect
from email.mime.text import MIMEText
import smtplib
from settings import TEMPLATE_DIRS


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact-form.html')
