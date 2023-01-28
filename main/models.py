from django.db import models

class Search(models.Model):
    search = models.CharField(blank=False, max_length=60)

class Person(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.name