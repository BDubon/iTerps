from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(db_column='course_ID', primary_key=True)  # Field name made lowercase.
    course_number = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    # times = models.CharField(max_length=20)
    # days = models.CharField(max_length=10)
    # seats = models.IntegerField()
    description = models.CharField(max_length=300)
    # setting = models.CharField(max_length=10)
    # location = models.CharField(max_length=10)
    credits = models.IntegerField()
    prerequisites = models.CharField(max_length=100)
    fulfillment = models.CharField(max_length=10)
    # section = models.CharField(max_length=5)

    def __str__(self):
        return self.course_number

    def __unicode__(self):
        return self.course_number

    def get_absolute_url(self):
        return f'/courses/{self.slug}'

    class Meta:
        managed = True
        db_table = 'course'


'''class CourseDetailAdmin(iTerps.ModelAdmin):
    list_display = ("course_ID", "course_number", "name", "description", "credits", "prerequisites", "fulfillment")'''


class CourseRating(models.Model):
    from professors.models import Professor
    rating_id = models.AutoField(db_column='rating_ID', primary_key=True)  # Field name made lowercase.
    course = models.ForeignKey(Course, db_column='course_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    student_email = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    rating = models.IntegerField(
        choices=(
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        )
    )
    comment = models.CharField(max_length=300)
    prof_id = models.ForeignKey(Professor, models.DO_NOTHING, db_column='prof_ID')  # Field name made lowercase.

    # def __str__(self):
        # return self.course

    class Meta:
        managed = True
        db_table = 'course_rating'


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Course.objects.filter(slug=slug).order_by('-course_ID')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().course_ID)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_course_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_course_receiver, sender=Course)


class CourseProf(models.Model):
    from professors.models import Professor
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_ID')  # Field name made lowercase.
    professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='professor_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'course_prof'

