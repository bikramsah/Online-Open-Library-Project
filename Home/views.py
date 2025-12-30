from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from Home.forms import upload_book_form
from django.contrib import messages
from Home.models import books
from pathlib import Path
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth import get_user_model



# Create your views here.

def Home(request):
    form=User()
    if request.method=='POST':
         user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
         user.save()
    context={
        'form': form,

    }
    return render(request, 'login.html', context)

def handel_book_upload(request):
    if request.method == 'POST':
        form_data = upload_book_form(request.POST, request.FILES)
        book_ext = request.FILES.get('book_file').name
        if Path(book_ext).suffix == '.pdf' or Path(book_ext).suffix == '.PDF':
            if form_data.is_valid():
                book_data = form_data.save(commit=False)
                book_data.author = request.user
                form_data.save()
                return messages.success(request, f"Uploaded file successfully...")
            else:
                return messages.error(request, "Failed to upload file...")
        else:
            messages.error(request, "Only pdf file format is accepted...")


@login_required(login_url='login')
def index(request):
    get_books = books.objects.all().order_by('-id')

    res = {
        'book_form': upload_book_form,
        'books': get_books,
    }
    if request.method == 'POST':
        handel_book_upload(request)

    return render(request, 'index.html', res)
    

@login_required(login_url='login')
def Authors(request):
    User = get_user_model()
    users = User.objects.all()
    
    res = {
        'book_form': upload_book_form,
        'users':users,
    }
    if request.method == 'POST':
        handel_book_upload(request)


    return render(request, 'Authors.html', res)


def About(request):
    res = {
       'book_form': upload_book_form,
    }
    if request.method == 'POST':
        handel_book_upload(request)


    return render(request, 'About.html', res)


@login_required(login_url='login')
def read_book(request):

    res = {}
    return render(request, 'read_book.html', res)


@login_required(login_url='login')
def categories(request, key):
    key = key
    keys = ('Poem', 'Article', 'Story' , 'Reports', 'Others')
    get_books = books.objects.all().filter(genre=key)   
    if key not in keys:
        get_search = books.objects.filter(book_name__contains=key)
        get_books = get_search
    if request.method == 'POST':
        handel_book_upload(request)

    res = {
        'book_form': upload_book_form,
        'books': get_books,
    }

    return render(request, 'index.html', res)


@login_required(login_url='login')
def profile(request):
    
    u_books = books.objects.filter(author=request.user.username)
    
    res = {
        'books':u_books
    }
    return render(request, 'Profile.html', res)


@login_required(login_url='login')
def dele(request, id):
    try:
        book = books.objects.get(id=id)
    except book.DoesNotExist:
        raise(Http404)
    if book.delete():
        messages.error(request, "Book deleted..")
        return redirect('Home:profile')
    return render(request, 'Profile.html')


@login_required(login_url='login')
def reco(request, key):
    reco_book = books.objects.filter(author=key)
    res = {
        'r_books':reco_book,
    }
    return render(request, 'index.html', res)
