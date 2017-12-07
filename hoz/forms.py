from django import forms
from .models import ReviewPost
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
