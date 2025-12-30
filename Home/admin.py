from django.contrib import admin
from Home.models import books
from Home.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display= ['username', 'email', 'password']

admin.site.register(books)
admin.site.register(User, UserAdmin)