from django.urls import path
from .views import home, investing, investingQuiz

urlpatterns = [
    path("", home,name="home"),
    path("investing", investing, name="investing"),
    path("investing/quiz", investingQuiz, name="investing quiz"),
]