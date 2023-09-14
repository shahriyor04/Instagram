from django.db import models
from django.db.models import Model, ForeignKey, CharField, DateTimeField, ImageField, CASCADE
from django.utils.timezone import now

from users.models import UserProfile


class Post(Model):
    user = ForeignKey(UserProfile, on_delete=CASCADE, related_name= 'posts')
    image = ImageField(upload_to='posts')
    description = CharField(max_length=250)
    create_data = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} '

    class Meta:
        ordering = ['-create_data']


class Like(models.Model):
    user = ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return f" {self.user} to {self.post}"


class Comment(models.Model):
    author = ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    message = CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.message}"

    class Meta:
        ordering = ['-create_data']


