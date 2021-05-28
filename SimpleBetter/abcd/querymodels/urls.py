from django.urls import path
from .views import home, PublisherList, PublisherDetail

app_name = 'querymodels'
urlpatterns = [
	path('home', home, name='home'),
	path('list/', PublisherList.as_view(), name='publishers-list'),
	path('<int:pk>/detail/', PublisherDetail.as_view(), name='publishers-detail'),
]