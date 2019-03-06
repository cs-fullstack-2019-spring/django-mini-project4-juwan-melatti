from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class GameCollector(models.Model):
    username = models.CharField(max_length=70)
    Password1 = models.CharField(max_length=70)
    Password2 = models.CharField(max_length=70)
    dateAccountCreated = models.DateField(default=timezone.now)
    userTableForeignKey = models.ForeignKey(User, on_delete=models.PROTECT,
                                            null=True, blank=True)

    def __str__(self):
        return self.username


class Game(models.Model):
    name = models.CharField(max_length=70)
    developer = models.CharField(max_length=70)
    dateMade = models.DateField()
    ageLimit = models.PositiveIntegerField()
    gameCreator = models.ForeignKey(GameCollector, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
