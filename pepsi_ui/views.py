from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Flavor
from .forms import update_forms
def main(request):
    return render(request,"main.html",{
        'data':Flavor.objects.all()
    })
    
def add_page(request):
    print(request)
    if request.method == "POST":
        name = request.POST.get("name")
        units = request.POST.get("units")
        posting_number = request.POST.get("posting_number")
        
        flavor = Flavor(name=name,units=units,posting_number=posting_number)
        flavor.save()
        return HttpResponse("sucess!<b> <a href=''>ADD More</a>")
    else:
        return render(request,"add_flavor.html")

def update(request,id):
    if request.method == "POST":
        flavor = Flavor.objects.get(id=id)
        flavor.units = request.POST.get("units")
        flavor.save()
        return redirect("main")

def update_form(request):
    if request.method == "POST":
        form = update_forms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<a href=''>Go Back!</a><h1>SUCESS✅</h1>")
        else:
            return  HttpResponse("<h1>Failed to download</h1>")
    else:
        form = update_forms()
        return render(request,'form.html',{'form':form})
    
