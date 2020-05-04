from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='images', verbose_name='Add an image')
    video = models.FileField(blank=True, null=True, upload_to='videos', verbose_name='Add a video')
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    docs = models.FileField(blank=True, upload_to='documents', verbose_name='Add a document')

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(verbose_name='Comment')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)



class Announcement(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    add_video = models.FileField(upload_to='videos/', null=True, verbose_name="Add Video")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})


