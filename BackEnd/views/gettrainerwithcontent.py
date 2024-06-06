# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.http import HttpResponse
from BackEnd.models.trainer import Trainer
import sys
import json


from BackEnd.models.gettrainerutil import GetTrainerUtil


class GettrainerWithcontent(TemplateView):

   # Retornamos todos los entrenamientos obteniendo los datos de sus claves foraneas
    def get(self, request , *args , **kwargs):


        trainer_with_content_JSON = []


        if request.user.is_authenticated:
            jsonObject = ''

            try:

                trainer_util = GetTrainerUtil()

                # Hay que hacer el filtrado de los ejercicios obteniendo el id del seleccionado
                id_trainer = request.GET.get('idTrainer')
                #id_day = request.GET.get('idDay')
                id_user = request.user.id

                trainer = Trainer.objects.get(id=id_trainer)
                total_days = trainer.totaldays

                days_list = trainer_util.get_days(total_days)
                day_list_array = []
                body_place_array = []

                # preparamos la lista de body places por entrenamiento y dia
                for day in days_list:

                    # Por cada dia obtenemos sus body places
                    bodyPlacesList = trainer_util.getbodyplaces_by_idtrainer_and_day(id_trainer, day['id'], id_user)

                    for body_place in bodyPlacesList:
                        exercises = trainer_util.get_exercises_in_trainer_by_idtrainer_idday_idbodyplace(id_trainer,day['id'],body_place['id'],id_user)
                        body_place_content = {'id' : body_place['id'], 'name' : body_place['label'], 'exercises' : exercises}
                        body_place_array.append(body_place_content)

                    content_in_day = {'dayId' : day['id'] , 'dayName' : day['label'] , 'bodyPlaces' : body_place_array}
                    day_list_array.append(content_in_day)

                    # vaciamos el array de bodyplaces con ejercicios
                    body_place_array = []

                trainer_with_content_JSON.append({'trainer' : {'id':trainer.id , 'description' : trainer.name , 'totaldays' : trainer.totaldays , 'content' : day_list_array }})

            except:
                 e = sys.exc_info()[0]
                 print " %s" % e

            return HttpResponse(json.dumps(trainer_with_content_JSON), content_type="application/json")


    class Meta:
        app_label = 'BackEnd'