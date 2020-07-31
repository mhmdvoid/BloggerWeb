from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
# from .utils import *
from taggit.managers import TaggableManager
from django.core.validators import FileExtensionValidator

class Writer(models.Model):

    # we do so because we wanna extend the feature and the things that a user can do that's why we put one to one so now user got a writer that got new feature
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    # pic_profile = models.ImageField()
    # other field like description and etc
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Posts(models.Model):
    post_title = models.CharField(max_length=100)
    post_body = models.TextField()
    post_pic = models.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])
    post_description = models.CharField(max_length=125)
    tags = TaggableManager()
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_edited = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        ordering = ['-date_created']
    def __str__(self):
        return self.post_title

# class PostPictures(models.Model):

#
# class Comments(models.Model):
#     commenter = models.ForeignKey(Writer, on_delete=models.CASCADE)
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE)
#     comment_content = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.commenter.user.username + 'comment'