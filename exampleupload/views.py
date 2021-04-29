# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import FileUpload, Ads
from .forms import UploadForm, SizeSelectForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage



# Create your views here.

def upload(request):
    if request.method == 'POST':
        print(request.POST)
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save()
        print(instance)
        form.save()
    return render(request, 'form.html', {
        "form": form,
    })


def file_list(request):
    queryset_list = Ads.objects.all()
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


def adss(request):
    try:
        if request.method == "POST":
            f = request.POST.get("name")
            print(f)

            l = request.POST.get("email")

            print(l)

            d = request.POST.get("subject")

            print(d)
            p = request.FILES['video']
            print(p)
            v = request.FILES['photo']
            print(v)

            fs = FileSystemStorage()
            video = fs.save(p.name, p)
            photo = fs.save(v.name, v)
            uploaded_video_url = fs.url(video)
            uploaded_photo_url = fs.url(photo)
            adss = Ads(name=f, email=l, subject=d, photo=v, video=p)

            adss.save()

            print("adss", adss)

            print("adss", adss)

            return render(request, 'index.html')

        else:

            return render(request, 'list.html')

        # return render(request, 'about.html')
    except Exception as e:
        print(str(e))

        return render(request, 'resize_detail.html')


def resized(request):
    return HttpResponse('This is a test')
