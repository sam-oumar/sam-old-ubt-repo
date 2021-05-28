from django.contrib import admin

# Register your models here.
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'message']