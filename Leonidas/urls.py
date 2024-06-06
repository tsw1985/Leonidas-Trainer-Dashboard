from django.conf.urls import patterns, include, url
from django.contrib import admin


from BackEnd.views.currentdatetime import current_datetime
from BackEnd.views.timeclass import TimeClass

from BackEnd.views.pruebaclass import PruebaClass

from BackEnd.views.vistaenfichero import VistaEnFicheroClass

#Vista crear entrenamiento
from BackEnd.views.createtrainer import CreateTrainer

#Obtener todos los entrenamientos
from BackEnd.views.gettrainers import GetAllTrainer

#Obtener todas las partes del cuerpo
from BackEnd.views.getbodyplaces import GetAllBodyPlaces

#Obtener ejercicios por parte del cuerpo
from BackEnd.views.getexercices import GetExercices

#Obtener todos los dias
from BackEnd.views.getdays import GetDays

#Obtener todos los tipos de ejercicios
from BackEnd.views.gettypeexercises import  GetAllTypeExercises

#Obtener todas las configuraciones de entrenamietos
from BackEnd.views.getconfigurationtrainer import GetConfigurationTrainers

#Asignar ejercicio a entrenamiento
from BackEnd.views.addexercisetotrainer import AddExerciseToTrainer

#Eliminar ejercicio asignado a entrenamiento
from BackEnd.views.deleteconfigurationtrainer import DeleteConfigurationTrainer

# Obtenemos las partes del cuerpo por id entrenamiento y dia
from BackEnd.views.gettrainerwithcontent import  GettrainerWithcontent



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/time/$', current_datetime),
    url(r'^admin/timeclass/$', TimeClass.as_view()),
    url(r'^admin/pruebaclass/$', PruebaClass.as_view()),
    url(r'^admin/vistafichero/$', VistaEnFicheroClass.as_view()),
    url(r'^admin/createtrainer/$', CreateTrainer.as_view()),
    url(r'^admin/gettrainers/$', GetAllTrainer.as_view()),
    url(r'^admin/getbodyplaces/$', GetAllBodyPlaces.as_view()),
    url(r'^admin/getexercices/$', GetExercices.as_view()),
    url(r'^admin/getdays/$', GetDays.as_view()),
    url(r'^admin/gettypeexercises/$', GetAllTypeExercises.as_view()),
    url(r'^admin/getconfigurationtrainers/$', GetConfigurationTrainers.as_view()),
    url(r'^admin/addexercisetotrainer/$', AddExerciseToTrainer.as_view()),
    url(r'^admin/deleteexercisetotrainer/$', DeleteConfigurationTrainer.as_view()),
    url(r'^admin/gettrainerwithcontent/$', GettrainerWithcontent.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)