from django.contrib import admin
from .models import Subject, SubjectImage

# @admin.register(SubjectImage)
class SubjectImageInline(admin.TabularInline):
    model = SubjectImage
    extra = 3

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['year', 'duration', 'matiere', 'classroom', 'coefficient', 'pdf_file', 'page_count']
    inlines = [SubjectImageInline]