from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ReviewPost, RequestPost, CallbackPost
from .forms import ReviewPostForm, RequestPostForm, CallbackPostForm

def main(request):
    posts_reviews = ReviewPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form_reviews = ReviewPostForm(request.POST)
        if form_reviews.is_valid():
            posts_reviews = form_reviews.save(commit=False)
            posts_reviews.published_date = timezone.now()
            posts_reviews.save()
            return redirect('main')
        form_request = RequestPostForm(request.POST)
        if form_request.is_valid():
            post_request = form_request.save(commit=False)
            post_request.published_date = timezone.now()
            post_request.save()
            return redirect('main')
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        form_reviews = ReviewPostForm()
        form_request = RequestPostForm()
        form_callback = CallbackPostForm()
    return render(request, 'hoz/main.html', {'posts_reviews': posts_reviews[:3], 'form_reviews': form_reviews, 'form_request': form_request, 'form_callback': form_callback})

# def callback(request, template):
#     if request.method == "POST":
#         form_callback = CallbackPostForm(request.POST)
#         if form_callback.is_valid():
#             callback_post = form_callback.save(commit=False)
#             callback_post.published_date = timezone.now()
#             callback_post.save()
#             return redirect('main')
#     else:
#         form_callback = CallbackPostForm()
#     return render(request, template, {'form_callback': form_callback})

def furniture(request):
    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        form_callback = CallbackPostForm()
    return render(request, 'hoz/furniture.html', {'form_callback': form_callback})

def mattress(request):
    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        form_callback = CallbackPostForm()
    return render(request, 'hoz/mattress.html', {'form_callback': form_callback})

def carpet(request):
    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        form_callback = CallbackPostForm()
    return render(request, 'hoz/carpet.html', {'form_callback': form_callback})

def price(request):
    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
        form_request = RequestPostForm(request.POST)
        if form_request.is_valid():
            post_request = form_request.save(commit=False)
            post_request.published_date = timezone.now()
            post_request.save()
            return redirect('main')
    else:
        form_callback = CallbackPostForm()
        form_request = RequestPostForm()
    return render(request, 'hoz/price.html', {'form_callback': form_callback, 'form_request': form_request,})

def reviews(request):
    posts_reviews = ReviewPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form_callback = CallbackPostForm(request.POST)
        if form_callback.is_valid():
            callback_post = form_callback.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        form_callback = CallbackPostForm()
    return render(request, 'hoz/reviews.html', {'posts_reviews': posts_reviews, 'form_callback': form_callback})
