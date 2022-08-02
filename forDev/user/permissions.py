from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # permissions.SAFE_METHODS : GET method 접근 ( 파일 수정 및 변환이 없기 때문에 True 반환 )
        if request.method in permissions.SAFE_METHODS:
            return True
        # GET 방식을 제외한 경우, User 가 일치한 경우만 수정·삭제 가 가능하도록 권한 처리
        return obj.user == request.user
