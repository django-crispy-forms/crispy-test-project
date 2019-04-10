# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render


def index(request):
    settings.CRISPY_TEMPLATE_PACK = 'bootstrap4'
    from bootstrap4.forms import HorizontalMessageForm, MessageForm

    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'bootstrap4/index.html',
                  {
                      'default_form': MessageForm(),
                      'horizontal_form': HorizontalMessageForm(),
                      'default_form_failing': MessageForm(data={}),
                      'horizontal_form_failing': HorizontalMessageForm(data={}),
                  })
