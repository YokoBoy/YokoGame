
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

from .forms import UserRegisterForm
from django.contrib import messages

from lessons.models import Lesson

menu = [
    {'title' : "Главная", 'url_name' : 'mainPage'},
    {'title' : "Сервисы", 'url_name' : 'services'},
    {'title' : "Уроки", 'url_name' : 'lesson_list'},
    {'title' : "Поддержка", 'url_name' : 'support'},
    {'title' : "Войти", 'url_name' : 'login'},
]


def mainPage(request):
    data = {
        'menu' : menu,
        'lesson' : Lesson.objects.get(pk=1),
        'lessons' : Lesson.objects.all(),
    }
    return render(request, 'users/mainPage.html', context=data)


def about(request):
    return HttpResponse("About")


def handle_uploaded_file(f):
    with open(f"lessons/media/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def services(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['img_file'])
    return render(request, 'users/viktorina_create.html', {'menu': menu})


def support(request):
    return HttpResponse("Support")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'menu': menu, })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lesson_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form, 'menu': menu, })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('lesson_list')

    return render(request, 'users/logout.html',  {'menu': menu})