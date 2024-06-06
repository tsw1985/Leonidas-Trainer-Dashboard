# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/admin')
def current_datetime(request):

    now = datetime.datetime.now()
    # enviamos el usuario online a la nueva vista
    user = request.user

    return render_to_response('current_datetime.html', {
                            'current_date':now ,
                            'nombreProgramador':'Gabriel' , 'user' : user})