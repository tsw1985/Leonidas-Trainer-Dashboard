# -*- coding: utf-8 -*-
from django.db import models
from BackEnd.models.typetrainer import TypeTrainer
from django.contrib.auth.models import User

class Trainer(models.Model):

    name = models.CharField(max_length=100)
    # typetrainer = models.ManyToManyField(TypeTrainer)
    typetrainer = models.ForeignKey(TypeTrainer)

    usergym = models.ForeignKey(User)
    totaldays = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'BackEnd'