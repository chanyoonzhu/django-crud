from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    # redirect instruction after posting a new post
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)]) # arg1-route
