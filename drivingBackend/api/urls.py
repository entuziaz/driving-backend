from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('questions/', views.QuestionList.as_view()),
    path('courses/', views.CourseList.as_view()),
]
