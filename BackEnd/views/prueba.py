# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.context_processors import csrf
from BackEnd.models.trainer import Trainer
from django.core import serializers
from django.http import HttpResponse
from BackEnd.models.autocomplete import Autocomplete
import sys
import json


class Prueba(TemplateView):
    # Retornamos todos los entrenamientos obteniendo los datos de sus claves foraneas
    def get(self, request , *args , **kwargs):

        if (request.user.is_authenticated):


            # jsonObject = serializers.serialize('json', all_trainers, indent=4, relations=('typetrainer',))
            # jsonObject = serializers.serialize('json', list_autocomplete, indent=4)
            # return HttpResponse(jsonObject, content_type="application/json")

            list_autocomplete = []
            auto1 = Autocomplete()
            auto1.item = 'itemAuto1'
            auto1.label = 'labelAuto1'

            auto2 = Autocomplete()
            auto2.item = 'itemAuto2'
            auto2.label = 'labelAuto2'

            auto3 = Autocomplete()
            auto3.item = 'itemAuto3'
            auto3.label = 'labelAuto3'

            auto4 = Autocomplete()
            auto4.item = 'itemAuto4'
            auto4.label = 'labelAuto4'

            auto5 = Autocomplete()
            auto5.item = 'itemAuto5'
            auto5.label = 'labelAuto5'

            list_autocomplete.append({'item': auto1.item, 'label': auto1.label})
            list_autocomplete.append({'item': auto2.item, 'label': auto2.label})

            return HttpResponse(json.dumps(list_autocomplete), content_type="application/json")

            # return HttpResponse(jsonObject, content_type="application/json")


    class Meta:
        app_label = 'BackEnd'


