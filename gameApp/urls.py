from django.urls import path
from . import views

urlpatterns = [
    path('login/index', views.index, name='index'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('confirmAccount/', views.confirmAccount, name='confirmAccount'),
    path('login/mygames/<int:id>', views.myGames, name='myGames'),
    path('login/mygames/addGame/', views.addGame, name='addGame'),

]
