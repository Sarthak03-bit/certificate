from django.db import models


class Certificate(models.Model):
    Name = models.CharField(max_length=50)
    Course = models.CharField(max_length=200)
