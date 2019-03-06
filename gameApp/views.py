from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import GameCollectorForm, GameForm, GameCollector, Game
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):  # default function
    if request.user.is_authenticated:  # if there is a user login

        userCollector = GameCollector.objects.filter(userTableForeignKey=request.user)  # grabs the game collector
        userGame = Game.objects.all()
        context = {
            'userCollector': userCollector,
            'userGame': userGame,

        }
        return render(request, 'gameApp/index.html', context)  # takes user to the index page
    else:
        return render(request, 'gameApp/index.html')  # takes user to the index page


def createAccount(request):  # create a new account
    newGameCollectorForm = GameCollectorForm()  # starts a blank form (get request)
    context = {

        'GCForm': newGameCollectorForm,
    }
    return render(request, 'gameApp/createAccount.html', context)  # renders to create an account page


def confirmAccount(request):  # message to confirm user is inside
    newGameCollectorForm = GameCollectorForm(request.POST)  # takes information from post method
    context = {

        'GCForm': newGameCollectorForm,
    }

    if request.POST['Password1'] == request.POST['Password2']:  # if the passwords match the user will be created
        User.objects.create_user(request.POST['username'], "", request.POST['Password1'])  # creates user and pass
        return render(request, 'gameApp/confirm.html', context)  # renders to conformation page

    else:
        newGameCollectorForm = GameCollectorForm(request.POST)  # holds the information
        message = "These passwords do not match."  # gives a message to the user that the passwords do not match
        context = {
            'GCForm': newGameCollectorForm,
            'message': message
        }
        return render(request, 'gameApp/createAccount.html',
                      context)  # goes back to create account page with information already filled in


# def myGames(request,id):
#     myGames = get_object_or_404(Game, pk=id)
#     myGames.save()
#     myGames = Game.object.all()
#     context = {
#         "myGames" : myGames,
#         "Game": Game
#     }
#     return render(request, 'gameApp/myGames.html', context)

@login_required
def addGame(request):
    addGame = GameForm()
    context = {
        "addGameForm": addGame
    }
    if request.method == "POST":

        Game.objects.create(request.POST["name"], request.POST['developer'], request.POST['dateMade'],
                            request.POST["ageLimit"], request.POST["gameCreator"])
        return HttpResponse("The World Shall Now Access Your Game")

        print('save')
        thisgame = Game.objects.create(name=request.POST["name"], developer=request.POST['developer'],
                                       dateMade=request.POST['dateMade'],
                                       ageLimit=request.POST["ageLimit"])
        return redirect('index')
    else:
        print('hi')

    return render(request, 'gameApp/createGame.html', context)
