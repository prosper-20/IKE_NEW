from django.urls import path
from .views import CoursesView, CoursesDetailView, CourseEnrollmentView


urlpatterns = [
    path("all/", CoursesView.as_view(), name="all-courses"),
    path("<slug:slug>/enroll/", CourseEnrollmentView.as_view(), name="coures-enroll"),
    path("<slug:slug>/", CoursesDetailView.as_view(), name="course-detail")
]