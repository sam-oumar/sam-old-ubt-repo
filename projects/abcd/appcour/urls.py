from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'appcour'
urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('creeruser/', views.creerUser, name='creeruser'),
    path('crmessage/', views.crmessage, name='crmessage'),
    path('crservice/', views.crservice, name='crservice'),
    path('crimputation/', views.crimputation, name='crimputation'),
    path('crconsultation/', views.crconsultation, name='crconsultation'),
    path('crservice_list/', views.ServiceListView.as_view(), name='crservice_list'),
    path('<int:crmsgid>/creditermsg/', views.creditermsg, name='creditermsg'),
    path('<int:crmsgid>/crdetail/', views.crdetail, name='crdetail'),
    path('<int:crmsgid>/crsupprimer/', views.crsupprimer, name='crsupprimer'),
    path('login/', auth_views.LoginView.as_view(template_name='appcour/pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='appcour/pages/logout.html'), name='logout'),
]