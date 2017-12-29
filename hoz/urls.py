from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from . import views
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from . import views


# from hoz.sitemaps import ReviewPostSitemap, RequestPostSitemap, CallbackPostSitemap


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^ru/$', views.main, name='main'),
    url(r'^ru/furniture/', views.furniture, name='furniture'),
    url(r'^ru/mattress/', views.mattress, name='mattress'),
    url(r'^ru/carpet/', views.carpet, name='carpet'),
    url(r'^ru/price/', views.price, name='price'),
    url(r'^ru/reviews/', views.reviews, name='reviews'),
    url(r'^ua/$', views.main, name='main'),
    url(r'^ua/furniture/', views.furniture, name='furniture'),
    url(r'^ua/mattress/', views.mattress, name='mattress'),
    url(r'^ua/carpet/', views.carpet, name='carpet'),
    url(r'^ua/price/', views.price, name='price'),
    url(r'^ua/reviews/', views.reviews, name='reviews'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]
