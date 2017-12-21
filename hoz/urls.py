from django.conf.urls import url, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^furniture/', views.furniture, name='furniture'),
    url(r'^mattress/', views.mattress, name='mattress'),
    url(r'^carpet/', views.carpet, name='carpet'),
    url(r'^price/', views.price, name='price'),
    url(r'^reviews/', views.reviews, name='reviews'),
    url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
]
