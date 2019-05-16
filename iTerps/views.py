from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "iTerps - HOME"
    context = {'title': my_title}
    if request.user.is_authenticated:
        context = {'title': my_title, 'my_list': [1, 2, 3, 4, 5]}

    return render(request, 'home.html', context)


def courses_page(request):
    return render(request, 'courses/course_list.html', {'title': 'Courses'})


def professors_page(request):
    return render(request, 'professors/professor_list.html', {'title': 'Professors'})

