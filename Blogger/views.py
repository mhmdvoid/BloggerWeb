from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
# from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import Response
from taggit.models import Tag
from django.template.loader import render_to_string


from .models import *
from .forms import PostModelForm
from django.contrib.auth.decorators import login_required
# from .serializers import *
#
# from django.paginator import Paginator, EmptyPage
from django.core.paginator import Paginator, EmptyPage
def homePage(request):
    all_tags = Tag.objects.all()
    # print(Tag.objects.get(slug='python'))
    # print(Posts.)

    all_posts = Posts.objects.all()
    # bunch_posts = ['Python', 'Java', 'Django', 'Stack DataStructure']
    # posts_body = ['Python is a great language for scripting and web development', 'Java is a very comprehensive language for student ', 'A great framework for rapid development', 'Last in firs out']
    # for post_title, posts_body2 in zip(bunch_posts, posts_body):
    #     Posts.objects.create(
    #         post_title=post_title,
    #         post_body=posts_body2,
    #         writer=request.user.writer
    #     ).save()
    context = {
        'posts': all_posts,
        'tags': all_tags,
    }
    return render(request, 'home-page.html', context)
# @login_required(login_url='account_login')
def postPage(request, slug):
    the_post = Posts.objects.get(slug=slug)
    # print(type(the_post))
    # the user will click then template i will put the object slug so whenever a button is clicked template will let me know which object has been clicked on

    context = {
        'the_post': the_post,
    }
    return render(request, 'post-page.html', context)
def catPage(request):
    return render(request, 'category-page.html')

def getSpecificTag(request, slug, ):
    tag = Tag.objects.get(slug=slug)
    # getting all posts got that tag
    all_tag_posts = Posts.objects.filter(tags=tag)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(all_tag_posts, 2)
    # two here stands for how many objects
    # shown in each page
    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
    # context = {
    #     'tag_posts': page,
    #     # 'tha_tag': the_tag,
    #     }
    context = {
        'the_tag': tag,
        'tag_posts': page
    }
    return render(request, 'cate_posts.html', context)


    # TODO: search features to search by a specific user and post and so that a a visitor could hit enter and search for a user

# def createPOST(request):
#     new_form = inlineformset_factory(Writer, Posts, fields=('post_title', 'post_body'), extra=1, can_delete=False)
#     form = new_form(queryset=Posts.objects.none(), instance=request.user.writer)
#     if request.method == 'POST':
#         form = new_form(request.POST,
#                         instance=request.user.writer)  # here if the method is POST which is True, write a new instance in the form that sent after taking the whole data from
#
#
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context = {
#         'form': form
#     }
#
#     return render(request, 'creatBlog.html', context)

# def createPost(request):
#     if request.method == 'POST':
#         post_title_ = request.POST.get('post_title')
#         post_desc = request.POST.get('post_desc')
#         post_tags = request.POST.get('tag').strip()
#         tags_sent = []
#         if ',' in post_tags:
#             tags_sent = post_tags.split(',')
#         elif ' ' in post_tags:
#             tags_sent = post_tags.split(' ')
#
#         post_content = request.POST.get("post_content")
#
#         the_current_post_created = Posts.objects.create(
#             post_title=post_title_,
#             post_description=post_desc,
#             post_body=post_content,
#             writer=request.user.writer,
#         )
#         the_current_post_created.save()
#         the_current_post_created.tags.add(*tags_sent)
@login_required(login_url='account_login')
def createPost(request):


    new_form = inlineformset_factory(Writer, Posts, can_delete=False, fields=('post_title', 'post_description', 'post_body', 'post_pic', 'tags'), extra=1)
    form = new_form(queryset=Posts.objects.none(), instance=request.user.writer)
    if request.method == 'POST':
        form = new_form(request.POST, request.FILES, instance=request.user.writer)
        if form.is_valid():
            items = form.save(commit=False)
            for item in items:
                print(item)
                item.save()
            form.save_m2m()


            return redirect('home')
    context = {
        'form': form,

    }
    return render(request, 'createPost.html', context)

def deletePost(request, pk_):


    the_post = Posts.objects.get(id=pk_)

    the_post.delete()
    return redirect('home')
