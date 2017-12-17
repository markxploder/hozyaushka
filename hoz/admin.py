from django.contrib import admin
from .models import ReviewPost, RequestPost, CallbackPost

admin.site.register(ReviewPost)
admin.site.register(RequestPost)
admin.site.register(CallbackPost)
