from django.conf import settings
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):

        exclude_paths = ['']

        if not request.user.is_authenticated:
            if not request.path == settings.LOGIN_URL \
                    and not request.path.split('/')[1] == 'admin' \
                    and not request.path.split('/')[1] == 'media' \
                    and not request.path.split('/')[1] == 'oauth':

                if request.path not in exclude_paths:
                    return redirect(settings.LOGIN_URL)
