from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    snippet = models.CharField(max_length=255, default= "Read More...")
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def  get_absolute_url(self):
        return reverse('index')



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)


    def __(self):
        return str(self.user)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()

    def __str__(self):
        return '%s %s' % (self.name, self.post.title)

 




