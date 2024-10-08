from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            name=user.first_name,
            email=user.email
        )
        
        subject = 'Welcome to DevSearch'
        body = 'Welcome aboard sailor, howdy?'
        
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False
        )

    else:
        print('profile aint created')



def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

def updateUser(sender, instance, created, **kwargs):
    user = instance.user

    if created == False:
        user.username = instance.username
        user.first_name = instance.name
        user.email = instance.email
        user.save()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
post_save.connect(updateUser, sender=Profile)