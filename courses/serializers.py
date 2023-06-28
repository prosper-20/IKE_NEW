from rest_framework import serializers
from .models import Courses
from account.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.SerializerMethodField("get_instructor_name")
    students = serializers.SerializerMethodField("get_students_name")
    
    class Meta:
        model = Courses
        fields = ["title", "slug", "instructor", "instructor_name", "students"]

    
    def get_instructor_name(self, obj):
        user = User.objects.get(email=obj.instructor.email)
        return user.username
    
    def get_students_name(self, obj):
        return StudentSerializer(obj.students.all(), many=True).data
    
