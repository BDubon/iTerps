from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import CommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.views.generic import (
    FormView,
    DetailView,
    TemplateView,
    ListView,
)

class CourseListView(ListView):
    model = Course
    paginate_by = 12
    template_name = 'courses/course_list.html'
    # queryset = Course.objects.all()  # <courses>/<modelname>_list.html


class CourseDetailView(FormMixin, DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    paginate_by = 10
    form_class = CommentForm

    def get_success_url(self):
        return reverse('courses:course_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'course': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.course = self.object
            obj.save()
            return super(CourseDetailView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Course.objects.filter(name__icontains=q)
        return super(SearchView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(SearchView, self).get_context_data(results=self.results, **kwargs)
