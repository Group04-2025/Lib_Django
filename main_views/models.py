from django.db import models
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=5000)
    rating = models.IntegerField()


    def __str__(self):
        return self.reviewer_name