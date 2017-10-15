from django.conf.urls import url
from app2 import views


app_name = 'app2'

urlpatterns = [

    url(r'^$',views.index,name="index"),
    url(r'^other/',views.other,name="other"),
    url(r'^relative/',views.relative,name="relative"),


]
