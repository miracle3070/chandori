from django.db import models
from account.models import CustomUser

# Create your models here.
category_select = (
    ('정보 게시판', '정보 게시판'),
    ('질문 게시판', '질문 게시판'),
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    #writer = models.CharField(max_length=20)
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=category_select, default='정보 게시판')
    content = models.TextField()
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

class Comment(models.Model):
    content = models.ForeignKey(Blog, on_delete = models.CASCADE)
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.CharField('comment', max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.comment