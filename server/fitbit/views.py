# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the server for HealtHII - Please use url calls to draw specific information and initiate server actions.")
