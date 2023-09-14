from django.db import models
from django.db.models import ForeignKey, CharField, DateTimeField, BooleanField, Model

from users.models import UserProfile


class Message(Model):
    sender = ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    receiver = ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver')
    message = CharField(max_length=1200)
    timestamp = DateTimeField(auto_now_add=True)
    is_read = BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
