from django.urls import path
from . import views
urlpatterns = [
    path("",views.data,name='data'),
    path("id/<int:id>",views.getid,name="getid"),
    path("update/<int:id>",views.update_async,name='updateapi'),
    path("add/<str:flavor>/<int:amount>",views.add_one,name='add'),
    path("delete",views.delete,name="deletes")
]