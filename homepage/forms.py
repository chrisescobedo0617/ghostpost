from django import forms
from homepage.models import Post

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['content', 'post_type']