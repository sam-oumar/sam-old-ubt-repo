from django.urls import path
from .import views
app_name = 'csvupload'
urlpatterns = [
    path('', views.contact_upload, name='contact_upload'),
]