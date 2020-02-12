from django.contrib import admin
from .models import Post


# Register your models here.
#to register the table post on your dashboard,pass post as an argument into the following command
admin.site.register(Post)
