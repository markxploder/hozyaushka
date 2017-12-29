from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main_ru', 'furniture_ru', 'carpet_ru', 'mattress_ru', 'price_ru', 'main_ua', 'furniture_ua', 'carpet_ua', 'mattress_ua', 'price_ua',]

    def location(self, item):
        return reverse(item)
