from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import CallbackPost
from .forms import CallbackPostForm

def callback_form(request):
    if request.method == "POST":
        callback_form = CallbackPostForm(request.POST)
        if callback_form.is_valid():
            callback_post = callback_form.save(commit=False)
            callback_post.published_date = timezone.now()
            callback_post.save()
            return redirect('main')
    else:
        callback_form = CallbackPostForm()
    return render(request, {'callback_form': callback_form})
