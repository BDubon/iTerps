from django.contrib import admin
from .models import Course, CourseProf, Rating

admin.site.register(CourseProf)


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_number', 'name', )
    search_fields = ('course_number', 'name', 'description')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'body', 'created', 'approved')
    search_fields = ('course', 'user', 'body')


admin.site.register(Course, CourseAdmin)
admin.site.register(Rating, RatingAdmin)

