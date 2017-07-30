from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)