from django.contrib import admin
from .models import  Company, Employees, Entry, Blog, Question, Reponse, Person

# Register your models here.
# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ["first_name", "last_name", "address", "number"]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name", "company"]
 
# @admin.register(Entry)    
# class EntryAdmin(admin.ModelAdmin):
# 	exclude = ["authors"]
# 	list_display = [field.name for field in Entry._meta.get_fields()]
	
admin.site.register(Person)
admin.site.register(Entry)
admin.site.register(Blog)
admin.site.register(Question)
admin.site.register(Reponse)