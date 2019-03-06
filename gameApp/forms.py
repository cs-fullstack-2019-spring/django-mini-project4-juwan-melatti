from django import forms
from .models import GameCollector,Game
import datetime

class GameCollectorForm(forms.ModelForm):
    class Meta:
        model=GameCollector
        exclude= ['userTableForeignKey','dateAccountCreated']




class GameForm(forms.ModelForm):
    class Meta:
        model=Game
        exclude=['gameCreator']
        widgets ={
            # 'dateMade': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            "dateMade": forms.SelectDateWidget()
        }


        def clean_dateMade(self):
            enteredDate=self.cleaned_data['dateMade']

            if enteredDate > datetime.date.today():
                raise forms.ValidationError("You can't choose a date in the future")
            return enteredDate

        def clean_ageLimit(self):
            enteredAge=self.cleaned_data['ageLimit']

            if enteredAge != 3 or enteredAge != 10 or enteredAge != 13 or enteredAge != 17 or enteredAge != 18:
                raise forms.ValidationError("The only valid entries for the age limit are 3, 10, 13, 17, and 18")
            return enteredAge