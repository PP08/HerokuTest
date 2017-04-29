from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hompage, name='homepage'),
    url(r'^database/$', views.test_database, name='test_db'),
]
