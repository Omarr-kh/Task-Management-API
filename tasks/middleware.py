from django.utils.deprecation import MiddlewareMixin
from .models import ActivityLog
from rest_framework.authentication import TokenAuthentication


class ActivityLogMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        authentication = TokenAuthentication()
        try:
            user, token = authentication.authenticate(request)
            ActivityLog.objects.create(
                user=user, endpoint=request.path, method=request.method
            )
        except:
            pass
        else:
            print("User is not authenticated or request is for admin path.")
