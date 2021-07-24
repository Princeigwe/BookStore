from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='slug')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pages:homepage_with_category', args=[self.slug])


class Book(models.Model):
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE, related_name='books', default=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, default='slug')
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='bookcover/', blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.pk])