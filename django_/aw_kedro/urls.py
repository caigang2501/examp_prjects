from django.urls import path
from . import views

app_name = "aw_kedro"
urlpatterns = [
    path("ali/", views.ali, name="ali"),
    path("", views.base, name="base"),
    path("register/", views.register, name="register"),
    path("awk/", views.tf_sentiment, name="tf_test"),
]

