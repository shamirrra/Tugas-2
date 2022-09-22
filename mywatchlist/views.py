from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import WatchList

def show_watch_list(request):
    data_watch_list = WatchList.objects.all()
    context = {
        'watch_list': data_watch_list,
        'name': 'Shamira',
        'student_id': '2106636376',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_watch_list = WatchList.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data_watch_list),
        content_type="application/xml")

def show_json(request):
    data_watch_list = WatchList.objects.all()
    return HttpResponse(
        serializers.serialize("json", data_watch_list),
        content_type="application/json")