# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render


def index(request):
    #settings.CRISPY_TEMPLATE_PACK = 'semantic_ui'
    from semantic.forms import HorizontalMessageForm, MessageForm

    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'semantic/index.html',
                  {'default_form': MessageForm(), 'horizontal_form': HorizontalMessageForm()})
