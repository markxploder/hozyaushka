from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.utils import timezone
from .models import ReviewPost, RequestPost, CallbackPost
from .forms import ReviewPostForm, RequestPostForm, CallbackPostForm
import telepot
from htmlmin.decorators import minified_response

bot = telepot.Bot('446407532:AAECo5m1NzzmGR-HE7LywBt2nlqTBsbOGt4')

@minified_response
def main(request):
    """ @Name           main page
        @About          rendering posts
                        rendering and validation forms
        @Params         reviews
                        request
                        callback
                        bot
        @Build          1.1
        @Author         riff_spliff
    """

    posts_reviews = ReviewPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form_reviews = ReviewPostForm(request.POST)
        if form_reviews.is_valid():
            posts_reviews = form_reviews.save(commit=False)
            posts_reviews.published_date = timezone.now()
            posts_reviews.save()
            return redirect('main_ru')
        form_request = RequestPostForm(request.POST)
        if form_request.is_valid():
            post_request = form_request.save(commit=False)
            post_request.published_date = timezone.now()
            post_request.save()

            bot.sendMessage(
                367977203, 'Новая заявка' + '\n'
                + '______________' + '\n\n'
                + 'Имя: ' + post_request.name + '\n'
                + 'Телефон: ' + post_request.phone + '\n'
                + 'Комментарий: ' + post_request.text)

            return redirect('main_ru')
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()

            bot.sendMessage(
                367977203, 'Перезвони мне!' + '\n'
                + '______________' + '\n\n'
                + 'Имя: ' + callback_post.name + '\n'
                + 'Телефон: ' + callback_post.phone)

            return redirect('main_ru')
    else:
        form_reviews = ReviewPostForm()
        form_request = RequestPostForm()
        form_callback = CallbackPostForm()
    return render(request, 'hoz/main.html', {'posts_reviews': posts_reviews[:3], 'form_reviews': form_reviews, 'form_request': form_request, 'form_callback': form_callback,})

@minified_response
def furniture(request):
    """ @Name           furniture page
        @About          rendering and validation forms
        @Params         callback
                        bot
        @Build          1.1
        @Author         riff_spliff
    """

    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()

            bot.sendMessage(
                367977203, 'Перезвони мне!' + '\n'
                + '______________' + '\n\n'
                + 'Имя: ' + callback_post.name + '\n'
                + 'Телефон: ' + callback_post.phone)

            return redirect('main_ru')
    else:
        form_callback = CallbackPostForm()
    return render(request, 'hoz/furniture.html', {'form_callback': form_callback})

@minified_response
def mattress(request):
    """ @Name           furniture page
        @About          rendering and validation forms
        @Params         callback
                        bot
        @Build          1.1
        @Author         riff_spliff
    """

    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()

            bot.sendMessage(
                367977203, 'Перезвони мне!' + '\n'
                + '______________' + '\n\n'
                + 'Имя: ' + callback_post.name + '\n'
                + 'Телефон: ' + callback_post.phone)

            return redirect('main_ru')
    else:
        form_callback = CallbackPostForm()
    return render(request, 'hoz/mattress.html', {'form_callback': form_callback})

@minified_response
def carpet(request):
    """ @Name           furniture page
        @About          rendering and validation forms
        @Params         callback
                        bot
        @Build          1.1
        @Author         riff_spliff
    """

    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()

            bot.sendMessage(
                367977203, 'Перезвони мне!' + '\n'
                + '______________' + '\n\n'
                + 'Имя: ' + callback_post.name + '\n'
                + 'Телефон: ' + callback_post.phone)

            return redirect('main_ru')
    else:
        form_callback = CallbackPostForm()
    return render(request, 'hoz/carpet.html', {'form_callback': form_callback})

@minified_response
def price(request):
    """ @Name           furniture page
        @About          rendering and validation forms
        @Params         callback
                        request
                        bot
        @Build          1.1
        @Author         riff_spliff
    """

    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()

            bot.sendMessage(
                367977203, 'Перезвони мне!' + '\n'
                + '______________' + '\n\n'
                + 'Имя: ' + callback_post.name + '\n'
                + 'Телефон: ' + callback_post.phone)

            return redirect('main_ru')
        form_request = RequestPostForm(request.POST)
        if form_request.is_valid():
            post_request = form_request.save(commit=False)
            post_request.published_date = timezone.now()
            post_request.save()
            return redirect('main_ru')
    else:
        form_callback = CallbackPostForm()
        form_request = RequestPostForm()
    return render(request, 'hoz/price.html', {'form_callback': form_callback, 'form_request': form_request,})

@minified_response
def reviews(request):
    """ @Name           furniture page
        @About          rendering posts
                        rendering and validation forms
        @Params         callback
                        bot
        @Build          1.1
        @Author         riff_spliff
    """

    posts_reviews = ReviewPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()

            bot.sendMessage(
                367977203, 'Перезвони мне!' + '\n'
                + '______________' + '\n\n'
                + 'Имя: ' + callback_post.name + '\n'
                + 'Телефон: ' + callback_post.phone)

            return redirect('main_ru')
    else:
        form_callback = CallbackPostForm()
    return render(request, 'hoz/reviews.html', {'posts_reviews': posts_reviews, 'form_callback': form_callback})

def error_404(request):
        response = render(request,'hoz/404.html')
        response.status_code = 404
        return response

def robots(request):
    return render(request, 'hoz/robots.txt')
