# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from BackEnd.models.days import Days

from django.http import HttpResponse
from BackEnd.models.autocomplete import Autocomplete
import sys
import json


class GetDays(TemplateView):
    # Retornamos todos los entrenamientos obteniendo los datos de sus claves foraneas
    def get(self, request , *args , **kwargs):

        if request.user.is_authenticated:
            jsonObject = ''

            try:


                list_autocomplete = []
                all_days = Days.objects.all().order_by('id')[:request.GET.get('limit')]

                print all_days

                # request.GET.get('find_text')

                # En este bucle creamos el objeto que necesita el jqueryUI Autocomplete
                for day_item in all_days:
                    list_autocomplete.append({'id': day_item.id, 'label': day_item.name})

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

    class Meta:
        app_label = 'BackEnd'



