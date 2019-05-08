from django import forms
from .models import Rating


class CommentForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('title', 'body')
