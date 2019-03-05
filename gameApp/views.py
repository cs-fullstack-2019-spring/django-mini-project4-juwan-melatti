from django.shortcuts import render, HttpResponse
from .forms import GameCollectorForm, GameForm, GameCollector, Game
from django.contrib.auth.models import User


# Create your views here.


# <<<<<<< HEAD
def index(request):
    return render(request, 'gameApp/index.html')


def createAccount(request):
    newGameCollectorForm = GameCollectorForm()
    context = {

        'GCForm': newGameCollectorForm,
    }
    return render(request, 'gameApp/createAccount.html', context)


def confirmAccount(request):
    newGameCollectorForm = GameCollectorForm(request.POST)
    context = {

        'GCForm': newGameCollectorForm,
    }

    if request.POST['Password1'] == request.POST['Password2']:
        User.objects.create_user(request.POST['username'], "", request.POST['Password1'])
        return render(request, 'gameApp/confirm.html', context)

    else:
        newGameCollectorForm = GameCollectorForm(request.POST)
        message = "These passwords do not match."
        context = {
            'GCForm': newGameCollectorForm,
            'message': message
        }
        return render(request, 'gameApp/createAccount.html', context)


def addGame(request):
    addGame = GameForm
    context = {
        "addGameForm": addGame
    }
    if request.method == "POST":
        Game.objects.create(request.POST["name"], request.POST['developer'], request.POST['dateMade'],
                            request.POST["ageLimit"], request.POST["gameCreator"])
        addGame.save()
        return HttpResponse("The World Shall Now Access Your Game")
    return render(request, 'gameApp/createGame.html', context)
