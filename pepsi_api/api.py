from .models import Flavor

def show():
    data = list(Flavor.objects.all().values())
    data = {i["name"]:i for i in data}
    return {"Flavor":data}
       
    
