from django import forms
from .models import Comment,Photo


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        # fields = ('title','image','description')
        exclude = ('user', 'users_like')
