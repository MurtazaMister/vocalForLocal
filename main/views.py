from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
import math, random
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.
def getTheme(request):
    theme = "light"
    if request.GET.get('isDark'):
        if request.GET.get('isDark')=="True":
            theme = "dark"
    return theme

def index(request):
    theme = getTheme(request)
    return render(request,'index.html',{'theme':theme})

def community(request):
    theme = getTheme(request)
    return render(request,'community.html',{'theme':theme,'token':os.getenv('MAP_ACCESS_TOKEN')})

def loginUser(request):
    pass

def logoutUser(request):
    pass

def signUp(request):
    theme = getTheme(request)
    return render(request, "signup.html", {'theme':theme,'csc_token':os.getenv('CSC_API_TOKEN')})

def generateEmailOTP():
    digits = os.getenv("DIGITS")
    OTP = ""
    otp_size = (int)(os.getenv("OTP_SIZE"))
    digits_len = (int)(os.getenv("DIGITS_LEN"))
    for i in range(otp_size) :
        OTP += digits[(math.floor(random.random() * digits_len))]
    return OTP

def sendEmailOtp(request):
    email=request.POST["email"]
    OTP = generateEmailOTP()
    html = '''
    <div style='font-family:system-ui;font-size:25px;width:max-content;'>
        <p style='text-align: center;'>Welcome to <span style='font-weight: 700;'>#vocalForLocal</span></p><br>
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