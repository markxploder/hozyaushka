from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^furniture/', views.furniture, name='furniture'),
    url(r'^mattress/', views.mattress, name='mattress'),
    url(r'^carpet/', views.carpet, name='carpet')
]
