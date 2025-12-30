from django import forms 
from django.forms import ModelForm
from .models import User
from Home.models import books

class upload_book_form(forms.ModelForm):
    class Meta:
        model = books
        fields = ['book_icon', 'book_name', 'book_description', 'book_file', 'genre']
        
class User(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password']