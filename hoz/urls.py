from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from . import views
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from . import views
from django.views.generic import RedirectView

# from hoz.sitemaps import ReviewPostSitemap, RequestPostSitemap, CallbackPostSitemap


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/ru/')),
    url(r'^furniture/', RedirectView.as_view(url='/ru/furniture')),
    url(r'^mattress/', RedirectView.as_view(url='/ru/mattress')),
    url(r'^carpet/', RedirectView.as_view(url='/ru/carpet')),
    url(r'^price/', RedirectView.as_view(url='/ru/price')),
    url(r'^ru/$', views.main, name='main_ru'),
    url(r'^ru/furniture/', views.furniture, name='furniture_ru'),
    url(r'^ru/mattress/', views.mattress, name='mattress_ru'),
    url(r'^ru/carpet/', views.carpet, name='carpet_ru'),
    url(r'^ru/price/', views.price, name='price_ru'),
    url(r'^ua/$', views.main, name='main_ua'),
    url(r'^ua/furniture/', views.furniture, name='furniture_ua'),
    url(r'^ua/mattress/', views.mattress, name='mattress_ua'),
    url(r'^ua/carpet/', views.carpet, name='carpet_ua'),
    url(r'^ua/price/', views.price, name='price_ua'),
    url(r'^ua/reviews/', views.reviews, name='reviews'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]
