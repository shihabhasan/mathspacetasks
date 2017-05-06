"""mathspaceTasks URL Configuration

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

from app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^help$', views.manual, name='help'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^task1_app$', views.task1_app, name='task1_app'),
    url(r'^task2_app$', views.task2_app, name='task2_app'),
    url(r'^task3_app$', views.task3_app, name='task3_app'),
    url(r'^api$', views.ApiView.as_view(), name='api'),
    url(r'^api/task1$', views.Task1ApiView.as_view(), name='task1_api'),
    url(r'^api/task2/n=(?P<n>[0-9]+)$', views.Task2ApiView.as_view(), name='task2_api'),
    url(r'^api/task3/city=(?P<city_name>[A-Za-z-]+)$', views.Task3ApiView.as_view(), name='task3_api'),
]
