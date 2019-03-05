from django.shortcuts import render,HttpResponse
from.forms import GameCollectorForm,GameForm,GameCollector,Game
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    newGameForm=GameForm()
    newGameCollectorForm=GameCollectorForm()
    context={
        'GForm':newGameForm,
        'GCForm':newGameCollectorForm,
    }
    return render(request,'gameApp/index.html',context)
