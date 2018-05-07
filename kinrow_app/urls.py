from django.conf.urls import url
from . import views

app_name = "kinrow_app"

urlpatterns = [
    url(r'^$', views.index, name="index"),
]
