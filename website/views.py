from django.shortcuts import render
from .models import Quiz

def home(request):
    return render(request, 'home.html')

def investing(request):
    return render(request, 'investing.html')

def investingQuiz(request):
    if request.method=="POST":
        print(request.POST)
        quest=Quiz.objects.filter(topic='Investing')
        score=0
        wrong=0
        correct=0
        total=0

        for q in quest:
            total+=1
            if q.correctAnswer == request.POST.get(q.title):
                score+=10
                correct+=1
            else:
                wrong+=1
        percentage = (correct/total)*100
        c = {"score":score, "correct":correct, "wrong":wrong, "percentage":percentage}
        return render(request, "investingQuizResult.html", c)
    quest =Quiz.objects.filter(topic='Investing')
    context ={"questions":quest}
    return render(request, "investingQuiz.html", context)

def about(request):
    return render(request, 'about.html')