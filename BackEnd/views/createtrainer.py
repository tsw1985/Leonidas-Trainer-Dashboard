# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.context_processors import csrf

from django.template import RequestContext



class CreateTrainer(TemplateView):


    def get(self, request , *args , **kwargs):
        c = {}
        c.update(csrf(request))
        template_name = 'createtrainer.html'
        return render_to_response(template_name ,c , context_instance = RequestContext(request))


    def post(self, request):
        c = {}
        c.update(csrf(request))
        template_name = 'createtrainer.html'
        return render_to_response(template_name,c)

    class Meta:
        app_label = 'BackEnd'