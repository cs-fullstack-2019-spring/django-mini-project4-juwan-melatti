from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('confirmAccount/', views.confirmAccount, name='confirmAccount'),
    path('addGame/', views.addGame, name='addGame'),

]
