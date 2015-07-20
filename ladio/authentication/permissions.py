from rest_framework import permissions

class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        if request.user:
            # 지금 요청하고 있는 사람이, 요청하고 있는 User 데이터를 소유한 사람이 맞는가?
            return user == request.user
        return False