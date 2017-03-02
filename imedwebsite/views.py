from django.shortcuts import render
from django.shortcuts import redirect
from email.mime.text import MIMEText
import smtplib
from settings import TEMPLATE_DIRS
from email.mime.text import MIMEText
import thread
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact-form.html')

def submit_email(request):
 #   if request.method == 'POST':

        #email = str(request.POST['email'])
        #name = str(request.POST['name'])
        #message = str(request.POST['message'])

        #if not (email or not name) and message:
        #    return redirect('index')

        #body = name + "," + email + "," + message

      msg = MIMEText(str(request.data))

      thread.start_new_thread(sendmail, (msg,))

       # return render(request, 'thankyou.html')
  # else:
   #     pass
      return HttpResponse('')
def sendmail(msg):
    MAILSERVER = smtplib.SMTP('outlook.office365.com', 587)
    MAILSERVER.starttls()
    MAILSERVER.ehlo()
    MAILSERVER.login("info@atumsoft.com", "\"d~XsN*9;+<Ec:ZB")
    FROMADDR = 'info@atumsoft.com'
    TOADDR = 'adam@imedmd.co'

    msg['Subject'] = 'Contact form received'
    msg['From'] = FROMADDR
    msg['To'] = TOADDR

    MAILSERVER.sendmail(FROMADDR, [TOADDR], msg.as_string())

    MAILSERVER.close()

def acuity(request):
    return redirect('https://vast-beyond-43297.herokuapp.com/')
