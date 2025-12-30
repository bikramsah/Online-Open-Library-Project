from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
#book models
class books(models.Model):
    GENRE = [
        ('Poem', 'Poem'),
        ('Story', 'Story'),
        ('Article', 'Article'),
        ('Report', 'Report'),
        ('Others', 'Others'),
    ]

    book_icon = models.ImageField(null=False, blank=False, upload_to='book_icon/')
    book_name = models.CharField(max_length=50, blank=False, null=False)
    book_description = models.TextField(blank=True, null=True)
    book_file = models.FileField(null=False, blank=False, upload_to='book_file/')
    author = models.CharField(max_length=25, blank=False, null=False)
    genre = models.CharField(choices=GENRE, max_length=20, null=False, blank=False)
    upload_date = models.DateField(default=timezone.now(), blank=True, null=False)

    def __str__(self):
        return self.book_name

#User models
class User(models.Model):
    username = models.CharField(null=False, blank=False, max_length=25)
    email = models.EmailField(max_length=30, blank=False, null=True)
    password = models.CharField(max_length=20, blank=False, null=True)    
    def __str__(self):
        return self.username
    
