from django.urls import path
from .views import SubjectListView, SubjectDetailView, UploadSubjectCsv

app_name = "subjects"
urlpatterns = [
    path("bac/sujets/<str:serie>", SubjectListView.as_view(), name="list_sujets"),
    path("bac/detail/<int:pk>", SubjectDetailView.as_view(), name="detail"),
    path("subject_upload", UploadSubjectCsv, name="subject_upload"),
]