from django import forms
from .models import ProfessorRating


class CommentForm(forms.ModelForm):
    class Meta:
        model = ProfessorRating
        fields = ('title', 'body')

