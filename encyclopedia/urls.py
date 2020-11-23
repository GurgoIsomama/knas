from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("add", views.add, name="add"),
    path("entry/<str:title>", views.entry, name="entry"),
]
