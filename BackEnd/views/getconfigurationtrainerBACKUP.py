# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from BackEnd.models.configurationtrainer import ConfigurationTrainer
from django.core import serializers
from django.http import HttpResponse
import sys


class GetConfigurationTrainers(TemplateView):

    # Retornamos todos los entrenamientos obteniendo los datos de sus claves foraneas
    def get(self, request , *args , **kwargs):

        # YA GUARDA EN BASE DE DATOS , LO QUE FALTA HACER ES EN JAVA SCRIPT LA CARGA DE LOS DATOS SEGUN SE GUARDA
        # Y MOSTRARLOS EN LA TABLA. UNA VEZ HECHO ESTO , TAMBIEN HACER LA FUNCION DE ELIMINARLO DE BASE DE DATOS
        # Y PRACTICAMENTE ESTARIA MAS O MENOS HECHO.



        if request.user.is_authenticated:
            jsonObject = ''

            try:
                # Hay que hacer el filtrado de los ejercicios obteniendo el id del seleccionado
                id_trainer = request.GET.get('idTrainer')
                id_day = request.GET.get('idDay')

                all_exercices = ConfigurationTrainer.objects.all()\
                                                            .select_related('exercise')\
                                                            .select_related('day')\
                                                            .select_related('trainer')\
                                                            .filter(usergym__username=request.user,\
                                                                    trainer__id=id_trainer,\
                                                                    day__id=id_day)

                #.order_by('exercise__bodyplace')\


                # Si queremos usar el json con todos los modelos relacionados tenemos que usar esta linea
                # y descomentar el return comentado de abajo.
                jsonObject = serializers.serialize('json', all_exercices, indent=4, relations=('exercise','day','trainer',))


            except:
                 e = sys.exc_info()[0]
                 print " %s" % e

            # Si queremos obtener el JSON normal con todos sus elementos relaciones hay que usar la linea comentada
            # lo que para este caso solamente vamos a usar el json.dumps para crear un json normal
            return HttpResponse(jsonObject, content_type="application/json")

    class Meta:
        app_label = 'BackEnd'

    class Trainer_JSON:
        id = 0
        description = ""
        listDay = []

    class Day_JSON:
        id = 0
        name = ""
        listBodyPlace = []

    class BodyPlace_JSON:
        id = 0
        name = ""
        listExercises = []

    class Exercise_JSON:
        id = 0
        name = ""
        description = ""



