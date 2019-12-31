from django.db import models

class ArticlePost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
