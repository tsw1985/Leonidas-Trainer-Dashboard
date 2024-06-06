# -*- coding: utf-8 -*-
from django.db import models
from BackEnd.models.typetrainer import TypeTrainer
# from django.contrib.auth.models import User

class Days(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'BackEnd'
