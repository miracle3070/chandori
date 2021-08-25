from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

class Post(models.Model):
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like=posts", blank= True)
