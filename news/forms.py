from django import forms
from .models import ArticleNew



class ArticleNewForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-input"}))

    class Meta:
        model = ArticleNew
        fields = [
            'title',
            'text',
            'views_count',
            'likes_users'

        ]

class ArticleEditForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-input"}))

    class Meta:
        model = ArticleNew
        fields = [
            'title',
            'text',
            'views_count',
            'likes_users'

        ]