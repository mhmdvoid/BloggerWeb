from django.db.models.signals import pre_save, post_save
from .utils import  unique_slug_generator2
from .models import *
from allauth.account.signals import user_signed_up

from django.contrib.auth import get_user_model

User = get_user_model()

# the name of the signal is the action you will be notified on


# def generateSlugPreSave(sender, instance, *args, **kwargs,):
#     if not instance.slug:
#         # if it does not exist
#         instance.slug = unique_slug_generator(instance)
#
# # pre_save.connect(generateSlugPreSave, sender=Tags)
def generateSlugPreSave2(sender, instance, *args, **kwargs,):
    if not instance.slug:
        # if it does notx exist
        instance.slug = unique_slug_generator2(instance)

pre_save.connect(generateSlugPreSave2, sender=Posts)





def user_signed_up_notification(request, user, **kwargs):
    Writer.objects.create(
        user=user,
        first_name=user.username,
        last_name=user.last_name,
        email=user.email,

    ).save()

user_signed_up.connect(user_signed_up_notification, sender=User)

