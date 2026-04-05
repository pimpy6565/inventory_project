from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()


urlpatterns = [
    path("",views.main,name="main"),
    path("add",views.add_page,name="add"),
    path("update/<int:id>",views.update,name="update"),
    path("form",views.update_form,name="update_form"),
    path("delete",views.delete_flavor,name='delete_flavor'),

]