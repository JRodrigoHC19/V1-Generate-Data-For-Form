from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gen/", views.generator, name="generator"),
    path("preview/", views.preview, name="preview"),
]