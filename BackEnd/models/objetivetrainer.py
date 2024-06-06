# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class ObjetiveTrainer(models.Model):
    name = models.CharField(max_length=100)
    usergym = models.ForeignKey(User)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'BackEnd'

