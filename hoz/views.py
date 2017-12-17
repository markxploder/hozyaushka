from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ReviewPost, RequestPost, CallbackPost
from .forms import ReviewPostForm, RequestPostForm, CallbackPostForm

def main(request):
    posts = ReviewPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form = ReviewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('main')
        form_request = RequestPostForm(request.POST)
        if form_request.is_valid():
            post_request = form_request.save(commit=False)
            post_request.published_date = timezone.now()
            post_request.save()
            return redirect('main')
        callback_form = CallbackPostForm(request.POST)
        if callback_form.is_valid():
            callback_post = callback_form.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        form = ReviewPostForm()
        form_request = RequestPostForm()
        callback_form = CallbackPostForm()
    return render(request, 'hoz/main.html', {'posts': posts[:3], 'form': form, 'form_request': form_request, 'callback_form': callback_form})

# def callback(request, template):
#     if request.method == "POST":
#         callback_form = CallbackPostForm(request.POST)
#         if callback_form.is_valid():
#             callback_post = callback_form.save(commit=False)
#             callback_post.published_date = timezone.now()
#             callback_post.save()
#             return redirect('main')
#     else:
#         callback_form = CallbackPostForm()
#     return render(request, template, {'callback_form': callback_form})

def furniture(request):
    if request.method == "POST":
        callback_form = CallbackPostForm(request.POST)
        if callback_form.is_valid():
            callback_post = callback_form.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        callback_form = CallbackPostForm()
    return render(request, 'hoz/furniture.html', {'callback_form': callback_form})

def mattress(request):
    if request.method == "POST":
        callback_form = CallbackPostForm(request.POST)
        if callback_form.is_valid():
            callback_post = callback_form.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        callback_form = CallbackPostForm()
    return render(request, 'hoz/mattress.html', {'callback_form': callback_form})

def carpet(request):
    if request.method == "POST":
        callback_form = CallbackPostForm(request.POST)
        if callback_form.is_valid():
            callback_post = callback_form.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        callback_form = CallbackPostForm()
    return render(request, 'hoz/carpet.html', {'callback_form': callback_form})

def reviews(request):
    if request.method == "POST":
        callback_form = CallbackPostForm(request.POST)
        if callback_form.is_valid():
            callback_post = callback_form.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        callback_form = CallbackPostForm()
    return render(request, 'hoz/reviews.html', {'callback_form': callback_form})
