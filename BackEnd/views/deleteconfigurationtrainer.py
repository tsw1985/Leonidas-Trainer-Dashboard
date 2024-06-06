# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from BackEnd.models.configurationtrainer import ConfigurationTrainer
from django.core import serializers
from django.http import HttpResponse
import sys


class DeleteConfigurationTrainer(TemplateView):

    # Retornamos todos los entrenamientos obteniendo los datos de sus claves foraneas
    def get(self, request , *args , **kwargs):

        if request.user.is_authenticated:

            try:
                id_configuration = request.GET.get('idConfigurationTrainer')
                ConfigurationTrainer.objects.get(id=id_configuration).delete()
            except:
                 e = sys.exc_info()[0]
                 print " %s" % e

            return HttpResponse(status=200)

    class Meta:
        app_label = 'BackEnd'





