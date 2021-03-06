from django.http.response import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect
from main.models import User
from dotenv import load_dotenv
from main.helper import generateEmailOTP, redirector
import os

load_dotenv()

def sendEmailOtp(request):
    email=request.POST["email"]
    OTP = generateEmailOTP()
    html = '''
    <div style='font-family:system-ui;font-size:25px;width:max-content;'>
        <p>Welcome to <span style='font-weight: 700;'>#vocalForLocal</span>'''
    if(len(User.objects.filter(email=email))):
        html += ''', <b>'''+User.objects.get(email=email).username+'''</b>'''
    html += '''</p><br>
        <div style='height:max-content;width:max-content;'>
            <p style='margin:5px;font-size: 15px;'>Please use this verification code to verify your Email ID</p><br>
            <p style='font-weight: 700;margin: 5px;font-size:20px;'>'''+OTP+'''</p><br>
            <p style='margin:5px;font-size: 15px;'>If you didn't request this, you can ignore this email or <a href='mailto:vocalForLocal2022@gmail.com'>let us know</a>.</p><br>
            <p style='margin:5px;font-size: 15px;'>Thanks!</p>
        </div>
    </div>
    '''
    message = '''Welcome to #vocalForLocal\nPlease use this verification code to verify your Email ID\n'''+OTP+'''If you didn't request this, you can ignore this email or let us know.\nThanks!'''
    send_mail('Verify your OTP for #vocalForLocal',message,os.getenv('EMAIL_HOST_USER'),[email], fail_silently=False,html_message=html)
    return HttpResponse(OTP)

def unameChecker(request):
    if request.method == "POST":
        return HttpResponse(len(User.objects.filter(username=request.POST["username"])))

def emailChecker(request):
    if request.method == "POST":
        return HttpResponse(len(User.objects.filter(email=request.POST["email"])))

def phoneChecker(request):
    if request.method == "POST":
        return HttpResponse(len(User.objects.filter(phone_number=request.POST["phno"])))

def reportEmail(request):
    email = request.POST['email']
    theme = request.POST['theme']
    feedback = request.POST['feedback']
    message = f'''Your business has been reported. Refer to the feedback provided by the customer: {feedback}'''
    send_mail('Reported!',message,os.getenv('EMAIL_HOST_USER'),[email,os.getenv('EMAIL_HOST_USER')], fail_silently=False,html_message=message)
    return redirect(redirector('/dashboard', theme))