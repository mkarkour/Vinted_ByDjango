"""vinted URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from vinted.views import login,welcome,logout,registration,registration_vendeur,showannonce,reservation,showannonce_filtre,showbanword,showhistorique,showblock

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$',login),
    url(r'^welcome$',welcome),
    url(r'^logout$',logout),
    url(r'^registration$',registration),
    url(r'^registration_vendeur$',registration_vendeur),
    url(r'^showannonce$',showannonce),
    url(r'^reservation$',reservation),
    url(r'^showannonce_filtre$',showannonce_filtre),
    url(r'^showbanword$',showbanword),
    url(r'^showhistorique$',showhistorique),
    url(r'^showblock$',showblock),
]
