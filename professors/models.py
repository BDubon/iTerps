from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from courses.models import Course


# Create your models here.
# from posts.models import Post

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

    class Meta:
        managed = True
        db_table = 'professor'


class ProfessorRating(models.Model):
    rating_id = models.AutoField(db_column='rating_ID', primary_key=True)  # Field name made lowercase.
    prof = models.ForeignKey(Professor, db_column='prof_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    student_email = models.CharField(max_length=100)
    time = models.DateTimeField()
    rating = models.IntegerField()
    comment = models.CharField(max_length=300)
    course = models.ForeignKey(Course, models.CASCADE, db_column='course_ID')  # Field name made lowercase.
    slug = models.SlugField(unique=True)

    class Meta:
        managed = True
        db_table = 'prof_rating'
