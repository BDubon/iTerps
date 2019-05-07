from django.shortcuts import render, get_object_or_404
from .models import Course, CourseRating
from django.views.generic import (
    CreateView,
    DetailView,
    TemplateView,
    UpdateView,
    ListView,
    DeleteView
)
from django.db.models import Q
import operator


class CourseListView(ListView):
    model = Course
    paginate_by = 12
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


class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Course.objects.filter(name__icontains=q)
        return super(SearchView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(SearchView, self).get_context_data(results=self.results, **kwargs)


class CourseSearchListView(CourseListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(CourseSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result
