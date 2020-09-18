from django.db import models

class News(models.Model):
   url = models.CharField(max_length=3000)