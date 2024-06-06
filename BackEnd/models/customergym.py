from django.db import models

from django.contrib.auth.models import User

from BackEnd.models.trainer import Trainer

class Customergym(models.Model):
    name = models.CharField(max_length=100)
    firstname = models.CharField(max_length=500)
    secondname = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    usergym = models.ForeignKey(User)


    trainer = models.ManyToManyField(Trainer)



    def __str__(self):
        return self.name

    class Meta:
        app_label = 'BackEnd'