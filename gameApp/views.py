from django.shortcuts import render,HttpResponse
from.forms import GameCollectorForm,GameForm,GameCollector,Game
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    newGameCollectorForm=GameCollectorForm()
    context={

        'GCForm':newGameCollectorForm,
    }
    return render(request,'gameApp/index.html',context)

def confirm(request):
    newGameCollectorForm=GameCollectorForm(request.POST)
    context={

        'GCForm':newGameCollectorForm,
    }

    if request.POST['Password1'] == request.POST['Password2']:
        return render(request, 'gameApp/confirm.html')
    else:
        return render(request,'gameApp/failure.html')
