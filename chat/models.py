from django.db import models

from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser

# from .model_managers import PersonManager

class CustomUser(AbstractUser):
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.username


class PersonManager(models.Manager):
    def get_or_new(self,me,other):
        if str(me) == str(other):
            return None
        u1 = CustomUser.objects.get(username=me)
        u2 = CustomUser.objects.get(username=other)
        # qs = Person.objects.get(Q(Q(user1=me) & Q(user2=other)) | Q(Q(user1=other) & Q(user2=me)))
        qs = Person.objects.filter(Q(Q(user1=u2) & Q(user2=u1)) | Q(Q(user1=u1) & Q(user2=u2)))
        # return qs
        if qs.count() >= 1:
            return qs
        else:
            if me != other:
                obj = Person.objects.create(user1=u1,user2=u2)
                # Message.objects.create(person=obj,user=me,message='hi')
                return obj,True
            None,False


class Person(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user2')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = PersonManager()
    def __str__(self):
        return f'{self.pk}'
    class Meta:
        ordering = ['timestamp']

class Message(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    message = models.TextField(blank=True,null=True)
    image_base64 = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)