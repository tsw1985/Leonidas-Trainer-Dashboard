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


class GetAllTrainer(TemplateView):
    # Retornamos todos los entrenamientos obteniendo los datos de sus claves foraneas
    def get(self, request , *args , **kwargs):

        if request.user.is_authenticated:
            jsonObject = ''

            try:

                list_autocomplete = []
                all_trainers = Trainer.objects.all()\
                               .select_related('typetrainer')\
                               .filter(name__icontains=request.GET.get('find_text'), usergym__username=request.user)

                # En este bucle creamos el objeto que necesita el jqueryUI Autocomplete
                for trainer_item in all_trainers:
                    autocomplete = Autocomplete()
                    autocomplete.item = trainer_item.id
                    autocomplete.label = trainer_item.name
                    list_autocomplete.append({'item': autocomplete.item, 'label': autocomplete.label ,'totaldays' : trainer_item.totaldays   })

                # Si queremos usar el json con todos los modelos relacionados tenemos que usar esta linea
                # y descomentar el return comentado de abajo.
                # jsonObject = serializers.serialize('json', all_trainers, indent=4, relations=('typetrainer',))


            except:
                 e = sys.exc_info()[0]
                 print " %s" % e

            # Si queremos obtener el JSON normal con todos sus elementos relaciones hay que usar la linea comentada
            # lo que para este caso solamente vamos a usar el json.dumps para crear un json normal
            # return HttpResponse(jsonObject, content_type="application/json")
            return HttpResponse(json.dumps(list_autocomplete), content_type="application/json")


    def post(self, request):
        c = {}
        c.update(csrf(request))
        template_name = 'createtrainer.html'
        return render_to_response(template_name, c)

    class Meta:
        app_label = 'BackEnd'

