from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .sitemaps import StaticViewSitemap

app_name = "kinrow_app"

sitemaps = {
    'post': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', views.index, name="index"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
