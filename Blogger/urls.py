from django.urls import path, include
from .views import *
from django.contrib.auth.views import TemplateView


urlpatterns = [
    path('', homePage, name='home'),
    path('post/<slug:slug>/', postPage, name='post_page'),
    path('category/<slug:slug>', getSpecificTag, name='category'),
    path('createBlog/', createPost, name='create'),
    path('delete/<pk_>', deletePost, name='delete'),
    path('d/', TemplateView.as_view(template_name='testSignUp.html'))
    ,
    # path('signup/', singUp)
]

