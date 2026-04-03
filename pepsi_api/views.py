from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Flavor_serializer
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import * 
from . import api

@api_view(["GET"])
def data(request):
    #return JsonResponse(api.show())
    flavor = Flavor.objects.all()
    flavor_api = Flavor_serializer(flavor)
    return Response(flavor_api)

def getid(request,id):
    try:
        flavor = Flavor.objects.get(id=id)
        return JsonResponse({'flavor':flavor.name,'units':flavor.units,'posting_number':flavor.posting_number})
    
    except Exception as e:
        return JsonResponse({'error':e})

def update_async(request,id):
        if request.method == "POST":
            flavor = Flavor.objects.get(id=id)
            flavor.units = request.POST.get("units")
            flavor.save()
            return JsonResponse({'flavor':flavor.name,'units':flavor.units,'posting_number':flavor.posting_number})
        
def add_one(request,flavor,amount):
    if request.method == "GET":
        flavor = Flavor.objects.get(name__iexact=flavor)
        flavor.units += amount
        flavor.save()
        return redirect('main')
    else:
        return JsonResponse({'ERROR':'faild to update'})