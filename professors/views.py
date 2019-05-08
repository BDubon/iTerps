from .models import Professor
from .forms import CommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.views.generic import (
    DetailView,
    ListView,
)


# Create your views here.
class ProfessorListView(ListView):
    model = Professor
    paginate_by = 9
    template_name = 'professors/professor_list.html'


class ProfessorDetailView(FormMixin, DetailView):
    model = Professor
    template_name = 'professors/professor_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    paginate_by = 10
    form_class = CommentForm

    def get_success_url(self):
        return reverse('professors:professor_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(ProfessorDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'professor': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.prof = self.object
            obj.save()
            return super(ProfessorDetailView, self).form_valid(form)
        else:
            return self.form_invalid(form)


