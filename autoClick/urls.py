from django.conf.urls import url
from django.urls import path
from .views import click, coordinate, button, autoClick1, inputClicks

urlpatterns = [
    url(r'^$', button),
    url(r'^click', click, name='click'),
    url(r'^coordinate', coordinate, name='coordinate'),
    url(r'^inputClicks', inputClicks, name='int'),

    path("", autoClick1.as_view(), name='add'),
]
