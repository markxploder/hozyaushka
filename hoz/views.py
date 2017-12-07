from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ReviewPost, RequestPost
from .forms import ReviewPostForm, RequestPostForm

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
    else:
        form = ReviewPostForm()
        form_request = RequestPostForm()
    return render(request, 'hoz/main.html', {'posts': posts[:3], 'form': form, 'form_request': form_request})

def furniture(request):
    return render(request, 'hoz/furniture.html', {})

def mattress(request):
    return render(request, 'hoz/mattress.html', {})
