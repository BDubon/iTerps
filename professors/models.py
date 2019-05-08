from __future__ import unicode_literals
from django.db.models.signals import pre_save
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from courses.models import Course


class Professor(models.Model):
    prof_id = models.AutoField(db_column='prof_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    office = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    picture = models.CharField(max_length=400)
    courses = models.CharField(max_length=400)

    def __str__(self):
        return self.last_name

    class Meta:
        managed = True
        ordering = ['last_name']
        db_table = 'professor'


class ProfessorRating(models.Model):
    rating_id = models.AutoField(db_column='rating_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='username')
    prof = models.ForeignKey(Professor, db_column='prof_ID', on_delete=models.CASCADE, related_name='comments')  # Field name made lowercase.
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
        managed = True
        ordering = ['-rating_id']
        db_table = 'prof_rating'


def create_slug(instance, new_slug=None):
    slug = slugify(instance.first_name)
    if new_slug is not None:
        slug = new_slug
    qs = Professor.objects.filter(slug=slug).order_by('last_name')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().prof_id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_course_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_course_receiver, sender=Course)