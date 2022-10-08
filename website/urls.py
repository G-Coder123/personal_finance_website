from django.urls import path
from .views import home, investing, investingQuiz, about

urlpatterns = [
    path("", home,name="home"),
    path("investing", investing, name="investing"),
    path("investing/quiz", investingQuiz, name="investing quiz"),
    path("about", about, name="about"),
]