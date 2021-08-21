from email import message
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1':"AmI Great",
        'variable2':"Nusta Cafe"
    }
    messages.success(request, "This is a test message.")
    return render(request, 'index.html', context)

def about(request):
   return render(request, 'about.html')

def services(request):
   return render(request, 'services.html')

def contact(request):
   if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          msg = request.POST.get('msg')
          contact = Contact(name=name, email=email, phone=phone, msg=msg, date=datetime.today())
          contact.save()
          messages.success(request, "You Message has be sent to the Django Bro's!")
   return render(request, 'contact.html')

