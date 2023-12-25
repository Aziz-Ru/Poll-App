from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='/'),
    path("user/",views.user,name="note/")
]

