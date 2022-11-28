from rest_framework.permissions import SAFE_METHODS, BasePermission


# permission: only owner can edit post/comment

class EditPermissions(BasePermission):
    message = "Only owner of post/comment can editing post/comment"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


# permission: only owner can delete post/comment

class DeletePermissions(BasePermission):
    message = "Only owner of post/comment can delete post/comment"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user