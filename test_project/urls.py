"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import path

from bootstrap3.views import index as bootstrap_3_preview
from bootstrap4.views import index as bootstrap_4_preview
from bulma.views import index as bulma_preview
from semantic.views import index as semantic_preview
from django_rendering.views import index as django_rendering_preview

urlpatterns = [
    path('', bootstrap_4_preview),
    path('django', django_rendering_preview, name='django_rendering.views.index'),
    path('bootstrap3', bootstrap_3_preview, name='bootstrap3.views.index'),
    path('bootstrap4', bootstrap_4_preview, name='bootstrap4.views.index'),
    path('bulma', bulma_preview, name='bulma.views.index'),
    path('semantic', semantic_preview, name='semantic.views.index'),
]
