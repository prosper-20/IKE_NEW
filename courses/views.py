from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Courses
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .permissions import EditCoursePermission

class CoursesView(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)



class CoursesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    permission_classes = [EditCoursePermission, IsAuthenticated]
    serializer_class = CourseSerializer
    lookup_field = "slug"
    



class CourseEnrollmentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request, slug, **kwargs):
        try:
            course = Courses.objects.get(slug=slug)
        except Courses.DoesNotExist:
            return Response({"Error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user = request.user

        new_user = course.students.add(user)
    

        return Response({"Success": "You've successfully enrolled"}, status=status.HTTP_202_ACCEPTED)
    

        



