#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext

def index(request):
    context = RequestContext(request)
    return render_to_response('profile/index.html', {}, context)

