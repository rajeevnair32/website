"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.urls import path
from django.contrib.flatpages import views as flatpages_views

from django.contrib import sitemaps
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^blog/',  include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    path('about-us/', flatpages_views.flatpage, {'url': '/about-us/'}, name='about'),
    path('terms/',    flatpages_views.flatpage, {'url': '/terms/' }, name='terms'),
    path('privacy/',  flatpages_views.flatpage, {'url': '/privacy/'}, name='privacy'),
]

urlpatterns += [
    path('sitemap.xml', sitemaps_views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', sitemaps_views.sitemap, 
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
