# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.context_processors import csrf


class PruebaClass(TemplateView):
    template_name = 'pruebaformulario.html'

    def get(self, request):
        c = {}
        c.update(csrf(request))
        template_name = 'pruebaformulario.html'
        print "SOY GET Prueba class"
        return render_to_response(template_name ,c)

    def post(self, request):
        c = {}
        c.update(csrf(request))
        template_name = 'pruebaformulario.html'
        print "SOY POST pueba class"
        return render_to_response(template_name,c)