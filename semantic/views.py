# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    #settings.CRISPY_TEMPLATE_PACK = 'semantic_ui'
    from semantic.forms import HorizontalMessageForm, MessageForm

    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'semantic/index.html',
                  {
                      'default_form': MessageForm(),
                      'horizontal_form': HorizontalMessageForm(),
                      'default_form_failing': MessageForm(data={}),
                      'horizontal_form_failing': HorizontalMessageForm(data={}),
                  })
