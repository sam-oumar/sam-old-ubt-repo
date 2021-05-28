from django.urls import path
from .views import Author, QuestionListView, reponse, HomeView, PersonListView, PersonCreateView, PersonDetailView, employee_listview, employee_detailview, question

app_name = "clbaseviews"
urlpatterns = [
	path("", HomeView.as_view(), name="home"),
    path("list_person", PersonListView.as_view(), name="list_person"),
    path("create_person", PersonCreateView.as_view(), name="create_person"),
    path("detail_person/<int:pk>", PersonDetailView.as_view(), name="detail_person"),
    path('employee_list/', employee_listview, name = 'employee_list'),
    path('employee_detail/<int:pk>', employee_detailview, name = 'employee_detail'),
    path('question/', question, name = 'question'),
    path('reponse/<slug:slug>/', reponse, name = 'reponse'),
    path('liste_question/', QuestionListView.as_view(), name = 'liste_question'),
    # path('author/', Author, name = 'author'),
]