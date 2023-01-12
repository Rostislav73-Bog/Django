from django.contrib import admin

from .models import My_model

@admin.register(My_model)
class Menu_admin(admin.ModelAdmin):
    list_display =('title', 'text_main', 'price')
    fields = ['title', 'text_main', 'price']

    print(fields)