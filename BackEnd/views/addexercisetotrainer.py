# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from BackEnd.models.exercises import Exercises
from BackEnd.models.trainer import Trainer
from BackEnd.models.days import Days
from BackEnd.models.bodyplace import BodyPlace

from BackEnd.models.configurationtrainer import ConfigurationTrainer
from django.http import HttpResponse
import sys
import json


class AddExerciseToTrainer(TemplateView):

    # Retornamos todos los entrenamientos obteniendo los datos de sus claves foraneas
    def get(self, request , *args , **kwargs):
        return HttpResponse("OK GET")

    def post(self, request, *args, **kwargs):

        try:
            # Desensamblados el JSON que viene desde la vista
            # para convertirla en un objeto ConfigurationTrainer
            # trainer = models.ForeignKey(Trainer)
            # exercise = models.ForeignKey(Exercises)
            # day = models.ForeignKey(Days)
            # usergym = models.ForeignKey(User)

            if request.user.is_authenticated:
                data=json.loads(request.body)
                trainerData=data['jsonData']
                elements = json.loads(trainerData)

                # Creamos el objeto para guardarlo
                configurationTrainer = ConfigurationTrainer()
                configurationTrainer.day = Days.objects.get(id=elements['idDaySelected'])
                configurationTrainer.exercise = Exercises.objects.get(id=elements['idExercise'])
                configurationTrainer.trainer = Trainer.objects.get(id=elements['idTrainer'])
                configurationTrainer.bodyplace = BodyPlace.objects.get(id=elements['idBodyPlaceSelected'])
                configurationTrainer.usergym = request.user

                ConfigurationTrainer.save(configurationTrainer)

        except:
            e = sys.exc_info()[0]
            print " %s" % e


        # return HttpResponse(status=200)
        return HttpResponse(status = 200)


    class Meta:
        app_label = 'BackEnd'





