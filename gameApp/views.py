from django.shortcuts import render,HttpResponse
from.forms import GameCollectorForm,GameForm,GameCollector,Game
from django.contrib.auth.models import User

# Create your views here.


def index(request): #default function
    return render(request,'gameApp/index.html')   #takes user to the index page

def createAccount(request):  #allows user to create an account (get request)

    newGameCollectorForm=GameCollectorForm() #creates a blank form for the account
    context={

        'GCForm':newGameCollectorForm,   #carries the form into a dictionary
    }
    return render(request,'gameApp/createAccount.html',context) #renders on the create account page

def confirmAccount(request):   #confirms if user-login is valid
    newGameCollectorForm=GameCollectorForm(request.POST)
    context={

        'GCForm':newGameCollectorForm, #dictionary
    }

    if request.POST['Password1'] == request.POST['Password2']:  #if the passwords match,
        User.objects.create(request.POST['username'],request.POST['Password1'])   #create the new user with username and password
        return render(request,'gameApp/confirm.html')  #renders on a conformation page

    else:
        newGameCollectorForm=GameCollectorForm(request.POST)   #holds all the information the user entered
        message="These passwords do not match."  #gives a message that the user
        context={
            'GCForm':newGameCollectorForm,
            'message':message
        }
        return render(request,'gameApp/createAccount.html',context)  #sends all entered information back to the create account page with an error message
