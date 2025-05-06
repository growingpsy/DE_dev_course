from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # 읽기 요청(GET, HEAD, OPTIONS)은 항상 허용
            return True
        
        return obj.owner == request.user # 쓰기 요청(PUT, DELETE)은 작성자만 허용
