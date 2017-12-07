from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ReviewPost
from .forms import ReviewPostForm

def main(request):
    posts = ReviewPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form = ReviewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('main')
    else:
        form = ReviewPostForm()
    return render(request, 'hoz/main.html', {'posts': posts[:3], 'form': form})

def furniture(request):
    return render(request, 'hoz/furniture.html', {})
