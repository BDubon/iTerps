from haystack import indexes
from courses.models import Course


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    course_number = indexes.CharField(model_attr='course_number')
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    slug = indexes.CharField(model_attr='slug')
    credits = indexes.IntegerField(model_attr='credits')
    prerequisites = indexes.CharField(model_attr='prerequisites')
    fulfillment = indexes.CharField(model_attr='fulfillment')

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
