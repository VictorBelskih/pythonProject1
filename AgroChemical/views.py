from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'AgroChemical/index.html' )

def about(request):
    return render(request, 'AgroChemical/about.html')

def analyspojv(request):
    return render(request, 'AgroChemical/analyspojv.html')

def analyswater(request):
    return render(request, 'AgroChemical/analyswater.html')

def analysudob(request):
    return render(request, 'AgroChemical/analysudob.html')

def analyskorm(request):
    return render(request, 'AgroChemical/analyskorm.html')

def gis(request):
    return render(request, 'AgroChemical/gis.html')

def securityplant(request):
    return render(request, 'AgroChemical/securityplant.html')