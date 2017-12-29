from django import forms
from .models import ReviewPost, RequestPost, CallbackPost
from django.forms import widgets
from hoz.choices import *


class ReviewPostForm(forms.ModelForm):
    """ @Package         hoz.forms
        @About           review and rating
        @Build           1.0
        @Author          riff_spliff
    """

    rating = forms.ChoiceField(choices=REVIEW_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = ReviewPost
        fields = ['author', 'text', 'rating']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Имя', 'pattern': '^[a-zA-ZА-Яа-яЁё\s]+$'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Комментарий'}),
        }


class RequestPostForm(forms.ModelForm):
    """ @Package         hoz.forms
        @About           standart order
        @Build           1.0
        @Author          riff_spliff
    """

    class Meta:
        model = RequestPost
        fields = ['name', 'phone', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'pattern': '^[a-zA-ZА-Яа-яЁё\s]+$'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'pattern': '^[+0-9]+$'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Комментарий'}),
        }


class CallbackPostForm(forms.ModelForm):
    """ @Package         hoz.forms
        @About           simple callback order
        @Build           1.0
        @Author          riff_spliff
    """

    class Meta:
        model = CallbackPost
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'pattern': '^[a-zA-ZА-Яа-яЁё\s]+$'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'pattern': '^[+0-9]+$'}),
        }

class MyForm(forms.Form):
    lang = forms.CharField(max_length=2)        
