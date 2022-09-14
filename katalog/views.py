from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    getCatalogs = CatalogItem.objects.all()
    context = {
        'name' : 'Shamira Alifanindya Prasetya',
        'student_id' : '2106636376',
        'katalog' : getCatalogs
    }
    return render(request, 'katalog.html', context)