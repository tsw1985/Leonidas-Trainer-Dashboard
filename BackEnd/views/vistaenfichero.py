# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.context_processors import csrf

class VistaEnFicheroClass(TemplateView):
    template_name = 'vistafichero.html'

    def get(self, request):
        c = {}
        c.update(csrf(request))
        template_name = 'vistafichero.html'
        return render_to_response(template_name ,c)

    def post(self, request):
        c = {}
        c.update(csrf(request))
        template_name = 'vistafichero.html'
        return render_to_response(template_name,c)

    class Meta:
        app_label = 'BackEnd'