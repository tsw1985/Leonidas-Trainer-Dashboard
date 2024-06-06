# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from BackEnd.models.trainer import Trainer
from BackEnd.models.customergym import Customergym


class CustomergymTrainer(models.Model):

    trainerForCustomer = models.ManyToManyField(Trainer)
    customergym = models.ManyToManyField(Customergym)
    usergym = models.ForeignKey(User)

    #def __str__(self):.

    #    return self.name

    class Meta:
        app_label = 'BackEnd'
