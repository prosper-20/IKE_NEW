from django.db import models
from account.models import User


class Courses(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    students = models.ManyToManyField(User, related_name="course_students", blank=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Courses"
        ordering = ["title"]

    def __str__(self):
        return self.title
    

