from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import GameCollectorForm, GameForm, GameCollector, Game
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):  # default function
    if request.user.is_authenticated:  # if there is a user login
        userCollector = GameCollector.objects.filter(username=request.user)  # grabs the game collector
        print(userCollector)
        userGame = Game.objects.filter(gameCreator_id=userCollector[0])
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
        newGameCollector = GameCollector.objects.create(username=request.POST["username"])
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
    addGame = GameForm(request.POST or None)
    context = {
        "addGameForm": addGame
    }
    userCollector = GameCollector.objects.filter(username=request.user)  # grabs the game collector
    print(userCollector)
    if request.method == "POST":
        print(request.POST)

        print('save')


        placeholder = request.POST['dateMade_year'] + '-' + request.POST['dateMade_month'] + "-" + request.POST[
            'dateMade_day']
        thisgame = Game.objects.create(name=request.POST["name"], developer=request.POST['developer'],
                                       dateMade=placeholder, ageLimit=request.POST["ageLimit"],
                                       gameCreator=userCollector[0])

        print(request.user)

        return redirect('index')
    else:
        print('hi')

    return render(request, 'gameApp/createGame.html',context)


def editGame(request, id):
    game = get_object_or_404(Game, pk=id)
    newGame = GameForm(request.POST, instance=game)
    if newGame.is_valid():
        newGame.save()
        return redirect("index")

    return render(request, "gameApp/createGame.html", {'addGameForm': newGame})


def deleteGame(request, id):
    game = get_object_or_404(Game, pk=id)
    if request.method == 'POST':
        game.delete()
        return redirect('index')

    return render(request, "gameApp/deleteGame.html", {"selectedGame": game})
