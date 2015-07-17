from rest_framework import permissions

class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        if request.user:
            # obj == DB에 저장된 사용자, request.user = 지금 요청을 하고 있는 사용자.
            # 같은가? true.
            return user == request.user
        return False