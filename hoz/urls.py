from django.conf.urls import url, include, handler404, handler500
from . import views
from django.views.generic import RedirectView

handler404 = 'hoz.views.handler404'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^furniture/', views.furniture, name='furniture'),
    url(r'^mattress/', views.mattress, name='mattress'),
    url(r'^carpet/', views.carpet, name='carpet'),
    url(r'^price/', views.price, name='price'),
    url(r'^reviews/', views.reviews, name='reviews'),
]
