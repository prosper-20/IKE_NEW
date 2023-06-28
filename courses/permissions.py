from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class EditCoursePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            raise PermissionDenied("You must be authenticated to edit courses.")

        # Check if the user is an instructor
        if not request.user.is_instructor:
            raise PermissionDenied("Only instructors are allowed to edit courses.")

        return True

    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            raise PermissionDenied("You must be authenticated to edit this course.")

        # Check if the user is an instructor
        if not request.user.is_instructor:
            raise PermissionDenied("Only instructors are allowed to edit this course.")

        # Additional logic to determine if the user can edit the course
        # You can customize this logic based on your specific requirements
        # For example, you can check if the user is the owner of the course
        if obj.instructor != request.user:
            raise PermissionDenied("You are not the instructor of this course.")

        return True
