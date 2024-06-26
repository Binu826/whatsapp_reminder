import random
import smtplib
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate 
from django.contrib import auth
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ProfileForm
from Whatapp_Reminder_App.models import *
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    #if request.method == 'POST':
        # name = request.POST['name']
        # password = request.POST['password']
        # user = auth.authenticate(name=name,password=password)
        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('signup')
        # else:
        #     context = {'msg_error': 'Invalid data'}
        #     return render(request, 'signup.html', context)
    return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST':
        user= UserDetails()
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.password = request.POST['password']
        user.company_name = request.POST['company-name']
        user.company_type = request.POST['company-type']
        user.address = request.POST['address']
        user.save()
        #messages.success(request, 'Successufully registered')
        return redirect('send_welcome_email')
    return render(request,'signup.html')

def send_welcome_email(request):
    HOST = 'smtp-mail.outlook.com'
    PORT = 587
 
    From_email = 'agneljosy1@outlook.com'
    To_email = 'agneljosy@gmail.com'
    Password = 'Agnel@1234'
 
    # HTML email content
    html_content = '''
                <!DOCTYPE html>
                <html>
                <head>
                <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style type="text/css">
                        body {
                            margin: 0;
                            padding: 0;
                            width: 100%;
                            font-family: Lato, sans-serif;
                            font-size: 18px;
                            background-color: #F5F8FA;
                        }
                        #email {
                            margin: auto;
                            width: 100%;
                            max-width: 600px;
                            background-color: #ffffff;
                        }
                        .header {
                            background-color: #00A4BD;
                            text-align: center;
                            padding: 20px;
                            color: #ffffff;
                        }
                        .content {
                            padding: 30px;
                        }
                        h1 {
                            font-size: 56px;
                            margin: 0;
                        }
                        h2 {
                            font-size: 28px;
                            font-weight: 900;
                            margin: 0 0 10px;
                        }
                        p {
                            font-weight: 100;
                            color:black;
                            margin: 0 0 15px;
                        }
                        .button {
                            background-color: #00A4BD;
                            color: #ffffff;
                            padding: 15px 25px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            border-radius: 5px;
                            margin-top: 20px;
                        }
                        @media screen and (max-width: 600px) {
                            .content {
                                padding: 20px;
                            }
                            h1 {
                                font-size: 32px;
                            }
                            h2 {
                                font-size: 24px;
                            }
                        }
            </style>
            </head>
            <body>
            <div id="email">
            <div class="header">
            <h1>Welcome!</h1>
            </div>
            <div class="content">
            <h2>Welcome to WhatsApp Reminder Assistant!</h2>
            <p>Hello [Customer Name],</p>
            <p>
                Thank you for signing up for WhatsApp Reminder Assistant. We are thrilled to have you on board!
            </p>
            <p>
                Our service will help you stay organized and never miss an important task or event again. With WhatsApp Reminder Assistant, you can easily set reminders and get notified directly on your WhatsApp.
            </p>
            <p>
                Click the button below to start exploring our features and set your first reminder.
            </p>
            <p style="text-align: center;">
            <a href="[Your Website URL]" class="button">Get Started</a>
            </p>
            <p>
                If you have any questions, feel free to reach out to our support team.
            </p>
            <p>
                Best regards,<br>
                The WhatsApp Reminder Assistant Team
            </p>
            </div>
            </div>
            </body>
            </html>
    '''
 
    # Create a MIME multipart message
    msg = EmailMultiAlternatives(
        subject="Welcome to WhatsApp Reminder Assistant!",
        from_email=From_email,
        to=[To_email],
    )
    msg.attach_alternative(html_content, "text.html")
 
    try:
        with smtplib.SMTP(HOST, PORT) as smtp:
            smtp.starttls()
            smtp.login(From_email, Password)
            smtp.sendmail(From_email, To_email, msg.as_string())
        return HttpResponse("[*] Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"[*] Error sending email: {e}")



def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('name')  # Assume user identifies themselves with username
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            try:
                user = UserDetails.objects.get(name=username)
                user.save()
                messages.success(request, 'Password reset successfully')
                return redirect(reverse('login'))  # Redirect to login page after success
            except UserDetails.DoesNotExist:
                messages.error(request, 'User does not exist.')
        else:
            messages.error(request, 'Passwords do not match.')

    
    return render(request, 'forgot_password.html')

def mainpage(request):
    return render(request,'main.html')

def contacts(request):
    return render(request,'contacts.html')

def profile(request,id):
    mem = get_object_or_404(UserDetails, id=id)
    return render(request, 'profile.html', {'mem': mem})
    


