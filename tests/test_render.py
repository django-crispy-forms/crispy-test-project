import pytest
from django.test import Client
from django.conf import settings

def test_render():
    c = Client()
    response = c.get('/')
    status = response.status_code
    assert status == 200
