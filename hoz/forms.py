from django import forms
from .models import ReviewPost, RequestPost, CallbackPost
from django.forms import widgets
from hoz.choices import *


class ReviewPostForm(forms.ModelForm):

    rating = forms.ChoiceField(choices=REVIEW_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = ReviewPost
        fields = ['author', 'text', 'rating']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Комментарий'}),
        }


class RequestPostForm(forms.ModelForm):

    class Meta:
        model = RequestPost
        fields = ['name', 'phone', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Комментарий'}),
        }


class CallbackPostForm(forms.ModelForm):

    class Meta:
        model = CallbackPost
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
        }
