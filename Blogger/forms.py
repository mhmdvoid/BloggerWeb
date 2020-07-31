from .models import Posts
from django.forms import ModelForm


class PostModelForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['post_title', 'post_body', 'post_description', 'post_pic', 'tags']
