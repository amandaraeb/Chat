from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Message(models.Model):
    ''' Message model that contains recipient and sender, which are
    references to Django's built in User model. Contains a time stamp
    for when message was sent, which is default to now.'''

    recipient = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='recipient')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='sender', null=True)
    sent = models.DateTimeField(default=now)
    message = models.TextField()
