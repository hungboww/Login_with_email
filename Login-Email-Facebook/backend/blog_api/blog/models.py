from django.db import models

# Create your models here.

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=255)
    article_description = models.TextField()
    article_image = models.ImageField(upload_to='blog/images')
    slug = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=255, default='Subham')
    short_description = models.TextField(default="")
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article_id} - {self.article_title}"

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_id}"