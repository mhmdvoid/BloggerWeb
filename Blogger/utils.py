import string
import random
from django.utils.text import slugify
# from .models import *
# from Blogger.models import Posts, Tags

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#
#
# def unique_slug_generator(instance, new_slug=None,):
#     """
#     This is for a Django project and it assumes your instance
#     has a model with a slug field and a title character (char) field.
#     """
#     # if type(instance) is "<class 'Blogger.models.Posts'>":
#     #     slug = slugify(instance.post_title)
#     #
#     # # else: type(instance) is "<class 'Blogger.models.Posts'>":
#     #     slug = slugify(instance.tag_name)
#
#
#     if new_slug is not None:
#         slug = new_slug
#     else:
#
#         slug = slugify(instance.tag_name)
#
#
#     # the name of the class that contains the slug field in this case is that Courses
#     model_class = instance.__class__
#     # getting into the class.slugField and check if the value exists in the objects
#     qs_exists = model_class.objects.filter(slug=slug).exists()
#     if qs_exists:
#         new_slug = "{slug}-{randstr}".format(
#             slug=slug,
#             randstr=random_string_generator(size=4)
#         )
#         return unique_slug_generator(instance, new_slug=new_slug)
#     return slug


def unique_slug_generator2(instance, new_slug=None, ):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    # if type(instance) is "<class 'Blogger.models.Posts'>":
    #     slug = slugify(instance.post_title)
    #
    # # else: type(instance) is "<class 'Blogger.models.Posts'>":
    #     slug = slugify(instance.tag_name)

    if new_slug is not None:
        slug = new_slug
    else:

        slug = slugify(instance.post_title)

    # the name of the class that contains the slug field in this case is that Courses
    model_class = instance.__class__
    # getting into the class.slugField and check if the value exists in the objects
    qs_exists = model_class.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug