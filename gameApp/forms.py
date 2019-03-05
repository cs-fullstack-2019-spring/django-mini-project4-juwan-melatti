from django import forms
from .models import GameCollector,Game

class GameCollectorForm(forms.ModelForm):
    class Meta:
        model=GameCollector
        exclude= ['userTableForeignKey','dateAccountCreated']




class GameForm(forms.ModelForm):
    class Meta:
        model=Game
        exclude=['gameCreator']