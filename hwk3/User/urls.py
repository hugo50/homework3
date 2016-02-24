from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = {
    url(r'^$',views.index, name='index'),
    url(r'^register/',views.register, name='register'),
    url(r'^login/',views.login,name='my_login'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^$',views.msg_index,name='msg_index'),
    url(r'^add/',views.add,name='add'),
    url(r'^list/',views.list_msg,name='list_msg'),
}
