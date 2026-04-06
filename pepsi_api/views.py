from django.shortcuts import render,redirect
from rest_framework import status
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
    flavor_api = Flavor_serializer(flavor,many=True)
    return Response(flavor_api.data)

@api_view(["GET"])
def getid(request,id):
    try:
        flavor = Flavor.objects.get(id=id)
        flavor_api = Flavor_serializer(flavor,many=False)
        return Response(flavor_api.data)
    
    except Exception as e:
        return Response({'error':"Dont Exist"})

@api_view(["PATCH"])
def update_async(request,id):
        if request.method == "PATCH":
            flavor = Flavor.objects.get(id=id)
            flavor.units = request.data.get("units")
            flavor.save()
            flavor_api = Flavor_serializer(flavor,many=False)
            return Response(flavor_api.data)

@api_view(["GET"])        
def add_one(request,flavor,amount):
    if request.method == "GET":
        flavor = Flavor.objects.get(name__iexact=flavor)
        flavor.units += amount
        flavor.save()
        return redirect('main')
    else:
        return Response({'ERROR':'faild to update'})
    
@api_view(["DELETE"])
def delete(request):
    flavor = Flavor.objects.get(pk = request.data.get("id"))
    if flavor:
        flavor.delete()
        return Response({"DElETE":"SUCCES"})
    else:
        return Response({"ERROR":"SOMETHING WRONG"})
    
@api_view(["POST"])
def create_flavor(request):
    try:
        name = request.data.get("name")
        units = request.data.get("units")
        posting = request.data.get("posting_number")
        
        flavor = Flavor.objects.create(
            name=name,
            units=units,
            posting_number=posting
        )
        serializer = Flavor_serializer(flavor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)