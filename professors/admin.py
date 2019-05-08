from django.contrib import admin
from .models import Professor, ProfessorRating
# Register your models here.


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'courses')
    search_fields = ('first_name', 'last_name', 'courses')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved', 'body', 'created')
    search_fields = ('user', 'created', 'body')


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(ProfessorRating, RatingAdmin)
