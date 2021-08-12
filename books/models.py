from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your models here.

class Genre(models.Model): # the genre model for genre category
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='slug')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pages:homepage_with_category', args=[self.slug])


class Book(models.Model): # the book info model
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
    
    class Meta:
        app_label = "books"


class Review(models.Model): # the review model
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review',)
    reviewer = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='book_reviewer')
    review = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return str(self.review)
