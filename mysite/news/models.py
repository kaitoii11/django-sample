from django.db import models

# Create your models here.
class article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)
    first = models.CharField(max_length=1)
    url = models.IntegerField()

    class Meta:
        db_table='sample'
        managed = False