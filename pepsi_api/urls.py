from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .serializers import Flavor_view

router = DefaultRouter()
router.register("flavor",Flavor_view,basename="flavor")
urlpatterns = [
    path("",views.data,name='data'),
    path("id/<int:id>",views.getid,name="getid"),
    path("update/<int:id>",views.update_async,name='updateapi'),
    path("add/<str:flavor>/<int:amount>",views.add_one,name='add'),
    path("delete",views.delete,name="deletes"),
    path("menu",include(router.urls))
]