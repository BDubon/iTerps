from .models import Professor
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView)


# Create your views here.
class ProfessorListView(ListView):
    model = Professor
    paginate_by = 9
    template_name = 'professors/professor_list.html'


class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'professors/professor_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

