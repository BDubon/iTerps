from django.contrib import admin
from .models import Course, CourseRating, CourseProf


# Register your models here.
admin.site.register(Course)
admin.site.register(CourseRating)
admin.site.register(CourseProf)
# iTerps.site.register(Course, CourseDetailAdmin)

