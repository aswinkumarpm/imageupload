# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import FileUpload
from .forms import UploadForm, SizeSelectForm
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def upload(request):
    if request.method == 'POST':
        print(request.POST)
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save()
        print(instance)
        form.save()
    return render(request, 'index.html', {
        "form": form,
    })


def file_list(request):
    queryset_list = FileUpload.objects.all()
    print(queryset_list)
    context = {
        "objects_list": queryset_list,
    }
    return render(request, 'list.html', context)


def size(request, id=None):
    instance = get_object_or_404(FileUpload, id=id)
    form = SizeSelectForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        size = cd.get('size')
        print(size)
        print("test")
        split = str(size).split('*')
        width = split[0]
        height = split[1]
        context = {
            "photo": instance.photo,
            "instance": instance,
            "form": form,
            "size": size,
            "height": height,
            "width": width,
        }
        return render(request, "resized_detail.html", context)

    print(id)
    context = {
        "photo": instance.photo,
        "instance": instance,
        "form": form,

    }
    return render(request, "resize_detail.html", context)



def resized(request):

    return HttpResponse('This is a test')

