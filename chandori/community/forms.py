from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm) :
    class Meta :
        model = Blog
        fields = ['title', 'category', 'content']

class CommentForm(forms.ModelForm):
    comment =forms.CharField(
        widget=forms.Textarea(attrs={'style':'width:100%; height:80px'}),
        label=''
    )

    class Meta:
        model = Comment
        fields = ('content',)