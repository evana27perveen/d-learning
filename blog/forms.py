from django.contrib.auth.forms import forms
from blog.models import PostModel


class PostForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': ''}))

    class Meta:
        model = PostModel
        exclude = ('author', )


class PostEditForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Blog Title'}))

    class Meta:
        model = PostModel
        exclude = ('author', )
