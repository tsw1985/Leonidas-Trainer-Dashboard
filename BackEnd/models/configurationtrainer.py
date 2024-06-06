# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from BackEnd.models.typeexercise import TypeExercise
from BackEnd.models.trainer import Trainer
from BackEnd.models.exercises import Exercises
from BackEnd.models.days import Days
from BackEnd.models.bodyplace import BodyPlace

class ConfigurationTrainer(models.Model):
    trainer = models.ForeignKey(Trainer)
    exercise = models.ForeignKey(Exercises)
    day = models.ForeignKey(Days)
    usergym = models.ForeignKey(User)
    bodyplace = models.ForeignKey(BodyPlace)

    #def __str__(self):
    #    return self.description

    class Meta:
        app_label = 'BackEnd'

