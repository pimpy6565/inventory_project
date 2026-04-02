from django.forms import ModelForm 

from .models import Flavor
class update_forms(ModelForm):
    class Meta:
        model = Flavor
        fields = '__all__'