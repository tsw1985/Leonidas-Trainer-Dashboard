# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.context_processors import csrf

from BackEnd.models.exercises import Exercises

from django.http import HttpResponse
from BackEnd.models.autocomplete import Autocomplete
import sys
import json


class GetExercices(TemplateView):

    # Retornamos todos los entrenamientos obteniendo los datos de sus claves foraneas
    def get(self, request , *args , **kwargs):

        if request.user.is_authenticated:
            jsonObject = ''

            try:

                # Hay que hacer el filtrado de los ejercicios obteniendo el id del seleccionado
                body_place = request.GET.get('body_place')
                name_exercise = request.GET.get('find_text')
                type_exercise = request.GET.get('type_exercise')

                list_autocomplete = []

                 #all_trainers = Trainer.objects.all()\
                 #              .select_related('typetrainer')\
                 #               .filter(name__icontains=request.GET.get('find_text'), usergym__username=request.user)


                if (name_exercise != ""):
                    #all_exercices = Exercises.objects.all().filter(usergym__username=request.user,\
                    #                                               bodyplace__id=body_place,\
                    #                                               typeexercise=type_exercise,\
                    #                                               name__icontains=name_exercise)

                    all_exercices = Exercises.objects.all()\
                                                    .select_related('bodyplace')\
                                                    .filter(usergym__username=request.user,\
                                                                   bodyplace__id=body_place,\
                                                                   typeexercise=type_exercise,\
                                                                   name__icontains=name_exercise)

                    # En este bucle creamos el objeto que necesita el jqueryUI Autocomplete
                    for exercice_item in all_exercices:
                        print "BOIDY PLACE %s " % exercice_item.bodyplace.description

                        list_autocomplete.append({'id': exercice_item.id,\
                                                  'label': exercice_item.name,\
                                                  'bodyplace' : exercice_item.bodyplace.description,\
                                                  'description': exercice_item.description})

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



