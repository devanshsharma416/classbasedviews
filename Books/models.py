from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null = True)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    count = models.CharField(max_length=10)

    # provide the slug automatically
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title