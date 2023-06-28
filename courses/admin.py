from django.contrib import admin
from .models import Courses

class CoursseAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "instructor"]
    list_filter = ["instructor", "title"]
    search_fields = ["title", "instructor"]
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(Courses, CoursseAdmin)
