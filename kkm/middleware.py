from django.conf import settings
from django.shortcuts import redirect

def RedirectMiddleware(get_response):

    def middleware(request):
        response = get_response(request)
        path = request.path
        for route in settings.ROUTES:
            source = route['source']
            destination = route['destination']
            if path == source:
                return redirect(destination)
        return response

    return middleware