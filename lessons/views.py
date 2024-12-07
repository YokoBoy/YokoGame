from django.shortcuts import render
from .models import Lesson
from django.http import HttpResponseNotFound

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Page Not Found! </h1>")