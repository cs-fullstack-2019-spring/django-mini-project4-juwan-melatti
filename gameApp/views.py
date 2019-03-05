from django.shortcuts import render,HttpResponse
from.forms import GameCollectorForm,GameForm,GameCollector,Game
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request,'gameApp/index.html')

def createAccount(request):

    newGameCollectorForm=GameCollectorForm()
    context={

        'GCForm':newGameCollectorForm,
    }
    return render(request,'gameApp/createAccount.html',context)

def confirmAccount(request):
    newGameCollectorForm=GameCollectorForm(request.POST)
    context={

        'GCForm':newGameCollectorForm,
    }

    if request.POST['Password1'] == request.POST['Password2']:
        User.objects.create(request.POST['username'],request.POST['Password1'])
        return render(request,'gameApp/confirm.html')

    else:
        newGameCollectorForm=GameCollectorForm(request.POST)
        message="These passwords do not match."
        context={
            'GCForm':newGameCollectorForm,
            'message':message
        }
        return render(request,'gameApp/createAccount.html',context)
