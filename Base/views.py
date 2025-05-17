from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        content=request.POST.get('content')
        print(name,email,number,content)

        if len(name)>=1 and  len(name)<=40:
            pass
        else:
            messages.error(request,'length of name should be grater than 0 and less than 40 characters')
            return render(request,'home.html')

        if len(email)>=1 and  len(email)<=40:
            pass
        else:
            messages.error(request,'invalid email try again!')
            return render(request,'home.html')

        if len(number)>2 and  len(number)==10 or len(number)==13:
            pass
        else:
            messages.error(request,'invalid number try again!')
            return render(request,'home.html')
        ins=models.Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank you for contacting me || your message has been saved.')
        print('data has been saved to database')
        print('The request is on pass')
    return render(request,'home.html')