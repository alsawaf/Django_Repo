from django.conf.urls import url
from app1 import views


urlpatterns = [

    url(r'^$',views.index,name="index"),
    url(r'^users/',views.users,name="users"),
    url(r'^form/',views.RegisterUser,name="form"),


]
