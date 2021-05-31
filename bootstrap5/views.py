# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render
from bootstrap5.models import WithFileField
import os

import errno

def index(request):
    settings.CRISPY_TEMPLATE_PACK = 'bootstrap5'
    from bootstrap5.forms import HorizontalMessageForm, MessageForm, FormWithFileField, HorizontalModelForm

    filename = '.' + ("/somedire" * 10)
    try:
        os.makedirs(filename)
    except FileExistsError as e:
        assert e.errno is errno.EEXIST
    filename += "/" + ("myfile-" * 10) + ".txt"
    with open(filename, "w") as f:
        f.write('Hello world')
    instance = WithFileField(my_file=filename)


    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'bootstrap5/index.html',
                  {
                      'model_form': FormWithFileField(
                          instance=instance,
                          prefix='model_form',
                      ),
                      'horizontal_model_form': HorizontalModelForm(
                          instance=instance,
                          prefix='horizontal_model_form',
                      ),
                      'default_form': MessageForm(
                          data=request.POST if request.method == "POST" else None,
                          prefix='default_form',
                      ),
                      'horizontal_form': HorizontalMessageForm(
                          data=request.POST if request.method == "POST" else None,
                          prefix='horizontal_form',
                      ),
                      'default_form_failing': MessageForm(
                          data={},
                          prefix='default_form_failing',
                      ),
                      'horizontal_form_failing': HorizontalMessageForm(
                          data={},
                          prefix='horizontal_form_failing',
                      ),
                  })
