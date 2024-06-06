# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.context_processors import csrf

from BackEnd.models.exercises import Exercises
from BackEnd.models.days import Days
from BackEnd.models.configurationtrainer import ConfigurationTrainer

from django.http import HttpResponse
from BackEnd.models.autocomplete import Autocomplete
import sys
import json
from django.core import serializers

class GetTrainerUtil:


    def getbodyplaces_by_idtrainer_and_day(self,idTrainer,idDay,idUser):

        body_places = []

        try:
            # Hay que hacer el filtrado de los ejercicios obteniendo el id del seleccionado
            id_trainer = idTrainer
            id_day = idDay
            id_user = idUser

            query = "select bplace.id , bplace.description \
                     from  BackEnd_bodyplace as bplace \
                     inner join BackEnd_configurationtrainer bconfig \
                     on bconfig.bodyplace_id = bplace.id \
                     where bconfig.usergym_id = '%s' and bconfig.day_id = '%s' and bconfig.trainer_id = '%s'  \
                     group by bplace.id" % (id_user , id_day , id_trainer);


            all_configurations = ConfigurationTrainer.objects.raw(query)

            # obtenemos los dias
            for configuration_trainer in all_configurations:
                print configuration_trainer.id
                body_places.append({'id' : configuration_trainer.id , 'label' : configuration_trainer.description})

        except:
            e = sys.exc_info()[0]
            print " %s" % e

        return body_places



    def get_days(self,limit):

        list_autocomplete = []

        try:

            # all_days = Days.objects.all().order_by('id')[limit]
            all_days = Days.objects.all().order_by('id')

            index = 0

            # En este bucle creamos el objeto que necesita el jqueryUI Autocomplete
            # for day_item in all_days:
            for day_item in all_days:
                if index < limit:
                    list_autocomplete.append({'id': day_item.id, 'label': day_item.name})

                index = index + 1

        except:
            e = sys.exc_info()[0]
            print " %s" % e

            # Si queremos obtener el JSON normal con todos sus elementos relaciones hay que usar la linea comentada
            # lo que para este caso solamente vamos a usar el json.dumps para crear un json normal
            # return HttpResponse(jsonObject, content_type="application/json")
        return list_autocomplete


    def get_exercises_in_trainer_by_idtrainer_idday_idbodyplace(self,id_trainer, id_day, id_body_place, id_user):

        body_places = []

        try:

            # Hay que hacer el filtrado de los ejercicios obteniendo el id del seleccionado

            query = " select conf.id as id_conf , exer.id , exer.description "\
                    " from BackEnd_exercises exer "\
                    " inner join BackEnd_configurationtrainer as conf on conf.exercise_id = exer.id" \
                    " where conf.trainer_id = '%s' "\
                    " and conf.bodyplace_id = '%s' "\
                    " and conf.day_id = '%s'"\
                    " and conf.usergym_id = '%s' " % (id_trainer, id_body_place, id_day, id_user )


            all_configurations = ConfigurationTrainer.objects.raw(query)

            # obtenemos los dias
            for configuration_trainer in all_configurations:
                print configuration_trainer.id
                body_places.append({'id' : configuration_trainer.id ,\
                                    'label' : configuration_trainer.description,\
                                    'idconf' : configuration_trainer.id_conf})

        except:
            e = sys.exc_info()[0]
            print " %s" % e

        return body_places


