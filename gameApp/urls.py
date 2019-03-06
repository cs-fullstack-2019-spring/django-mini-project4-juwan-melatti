from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('confirmAccount/', views.confirmAccount, name='confirmAccount'),
    # path('login/mygames/<int:id>', views.myGames, name='myGames'),
    path('addGame/', views.addGame, name='addGame'),
    path('addGame/editGame/<int:id>/', views.editGame, name="editGame"),
    path("addGame/deleteGame/<int:id>/", views.deleteGame, name="deleteGame")

]
