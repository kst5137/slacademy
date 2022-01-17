from django.db import models

# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

