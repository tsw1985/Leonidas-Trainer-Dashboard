# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from BackEnd.models.bodyplace import BodyPlace
from BackEnd.models.typeexercise import TypeExercise

class Exercises(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    bodyplace = models.ForeignKey(BodyPlace)
    typeexercise = models.ForeignKey(TypeExercise)
    usergym = models.ForeignKey(User)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'BackEnd'