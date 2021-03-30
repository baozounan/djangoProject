"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views,search,search2,index
from django.contrib import admin

urlpatterns = [
    path('index/', index.index),
    path('index/openfg/', index.open_fg),
    path('index/send_message/', index.send_message),
    path('upload/',index.upload),
    path('hello/', views.hello),
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search-post/',search2.search_post),
    path('admin/',admin.site.urls),

]