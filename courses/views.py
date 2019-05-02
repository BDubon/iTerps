from django.shortcuts import render, get_object_or_404
from .models import Course, CourseRating
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
# Create your views here.


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    # queryset = Course.objects.all()  # <courses>/<modelname>_list.html


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'


# Probably won't work
class CommentForm(DetailView):
    model = CourseRating
    template_name = 'courses/courses_popupform.html'


    '''def get_object(self):
        course_id_ = self.kwargs.get('course_id')
        return get_object_or_404(Course, id=course_id_)'''
