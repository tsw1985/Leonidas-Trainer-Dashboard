from django.contrib import admin
from django.contrib.auth.models import User
from BackEnd.models.objetivetrainer import ObjetiveTrainer
from BackEnd.models.trainer import Trainer
from BackEnd.models.exercises import Exercises
from BackEnd.models.customergym import Customergym
from BackEnd.models.typetrainer import TypeTrainer
from BackEnd.models.bodyplace import BodyPlace
from BackEnd.models.days import Days
from BackEnd.models.typeexercise import TypeExercise
from BackEnd.models.configurationtrainer import ConfigurationTrainer

from BackEnd.models.customergymTrainer import CustomergymTrainer

class TrainerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    # Con esta etiqueta activo el filtrado horizontal para crear ejercicios
    # a el entrenamiento
    filter_horizontal = ['exercises']
    list_filter = ['name']


# Cuando se crean nuevos modelos hay que ponerlos tambien en el archivo
# init.py que esta dentro de backend/models/init.py


# Con esto hacemos que en la tabla de ejercicios solo se pongan los del usuario logueado
# para ello en los modelos tenemos que asociarles el usuario del sistema
class ExerciseAdmin(admin.ModelAdmin):

    # filter_horizontal = ['bodyplace']

    def queryset(self, request):
        qs = super(ExerciseAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usergym=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usergym" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
            return db_field.formfield(**kwargs)
        return super(ExerciseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



class ObjetiveTrainerAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(ObjetiveTrainerAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usergym=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usergym" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
            return db_field.formfield(**kwargs)
        return super(ObjetiveTrainerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class TrainerAdmin(admin.ModelAdmin):

    # filter_horizontal = ['typetrainer']

    def queryset(self, request):
        qs = super(TrainerAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usergym=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usergym" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
            return db_field.formfield(**kwargs)
        return super(TrainerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class CustomerGymAdmin(admin.ModelAdmin):

    filter_horizontal = ['trainer']

    def queryset(self, request):
        qs = super(CustomerGymAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usergym=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usergym" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
            return db_field.formfield(**kwargs)
        return super(CustomerGymAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class TypeTrainerAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(TypeTrainerAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usergym=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usergym" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
            return db_field.formfield(**kwargs)
        return super(TypeTrainerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class BodyPlaceAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(BodyPlaceAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usergym=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usergym" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
            return db_field.formfield(**kwargs)
        return super(BodyPlaceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class TypeExerciseAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(TypeExerciseAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usergym=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usergym" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(username=request.user)
            return db_field.formfield(**kwargs)
        return super(TypeExerciseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)






# class CustomergymTrainerAdmin(admin.ModelAdmin):
    # search_fields = ['name']
    # Con esta etiqueta activo el filtrado horizontal para crear ejercicios
    # a el entrenamiento
    # filter_horizontal = ['trainerForCustomer']
    # filter_horizontal = ['customergym']
    #filter_horizontal = ['trainer']

#    def queryset(self, request):
#        qs = super(CustomergymTrainerAdmin, self).queryset(request)
#        if request.user.is_superuser:
#            return qs
#        return qs.filter(usergym=request.user)

#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == "usergym" and not request.user.is_superuser:
#            kwargs["queryset"] = User.objects.filter(username=request.user)
#            return db_field.formfield(**kwargs)
#        return super(CustomergymTrainerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


    # list_filter = ['name']


#Aqui registramos los cambios para cada clase, de como queremos que se vea en el admin
admin.site.register(Exercises, ExerciseAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(ObjetiveTrainer, ObjetiveTrainerAdmin)
admin.site.register(Customergym, CustomerGymAdmin)
admin.site.register(TypeTrainer, TypeTrainerAdmin)
admin.site.register(BodyPlace, BodyPlaceAdmin)
admin.site.register(Days)
admin.site.register(TypeExercise,TypeExerciseAdmin)
admin.site.register(ConfigurationTrainer)

# admin.site.register(CustomergymTrainer, CustomergymTrainerAdmin)

# admin.site.register(Exercises)

# Esto es para filtrar ciertos campos
#class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date' , 'question']

#class CocheAdmin(admin.ModelAdmin):
    #fields = ['marca','motor','modelo','color']

#admin.site.register(Poll, PollAdmin)