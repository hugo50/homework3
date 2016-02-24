"""hwk3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from User.views import index,register,my_login,my_logout,add,list_msg,msg_index

urlpatterns = [
    url(r'^user/$',index),
    url(r'^user/login/$',my_login),
    url(r'^user/logout/$',my_logout),
    url(r'^user/register/$',register),
    url(r'^message/$',msg_index),
    url(r'^message/add/$',add),
    url(r'^message/list/$',list_msg),
    url(r'^admin/', admin.site.urls),
]
