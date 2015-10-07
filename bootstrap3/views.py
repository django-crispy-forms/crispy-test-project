# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render


def index(request):
    settings.CRISPY_TEMPLATE_PACK = 'bootstrap3'
    from bootstrap3.forms import MessageForm
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'index.html', {'form': MessageForm()})
