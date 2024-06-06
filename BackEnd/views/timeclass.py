# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

class TimeClass(TemplateView):
    template_name = 'current_datetime.html'

    def get(self, request):
        template_name = 'current_datetime.html'
        user = request.user
        print "SOY GET"
        values = {'nombreProgramador':'Gabriel USA EL GET' , 'user' : user}
        return render_to_response(template_name , values)


    def post(self, request):
        user = request.user
        values = { 'nombreProgramador':'Gabriel USA EL POST' , 'user' : user}
        template_name = 'current_datetime.html'
        print "SOY POST"

        return render_to_response(template_name , values)


    def saludoFuncion(self,request):
        return render_to_response('esto es un saludo')