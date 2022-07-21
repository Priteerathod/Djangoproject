from django.db import models
from django.urls import reverse
# Create your models here.
class client(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100)
    cdate=models.DateField()
    cby=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.id})
