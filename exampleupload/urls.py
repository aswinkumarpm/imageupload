from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from .views import (
    upload,
    file_list,
    size,resized
)


urlpatterns = [
    url(r'^upload$', upload, name='upload'),
    url(r'^file_list$', file_list, name='file_list'),
    url(r'^(?P<id>\d+)/$', size, name='size'),
    url(r'^resized$', resized, name='resized$'),

]