from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models import Q


class Course(models.Model):
    # Field name made lowercase.
    course_number = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=300)
    credits = models.IntegerField()
    prerequisites = models.CharField(max_length=100)
    fulfillment = models.CharField(max_length=10)

    def __str__(self):
        return self.course_number

    def get_absolute_url(self):
        return f'/courses/{self.slug}'

    class Meta:
        managed = True


class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')  # Field name made lowercase.
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='username')
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-created']
        managed = True


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Course.objects.filter(slug=slug).order_by('-course_ID')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().course_id)
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

