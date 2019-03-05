from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import GameCollectorForm, GameForm, GameCollector, Game
from django.contrib.auth.models import User


# Create your views here.



def index(request): #default function
    if request.user.is_authenticated:
        userGame= GameCollector.objects.filter(userTableForeignKey=request.user)
        context= {
        'userGame':userGame
         }
        return render(request,'gameApp/index.html',context)   #takes user to the index page
    else:
        return render(request,'gameApp/index.html')   #takes user to the index page




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

def myGames(request,id):
    myGames = get_object_or_404(Game, pk=id)
    myGames.save()
    myGames = Game.object.all()
    context = {
        "myGames" : myGames,
        "Game": Game
    }
    return render(request, 'gameApp/myGames.html', context)


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

    return redirect(request, 'gameApp/index.html', context)

