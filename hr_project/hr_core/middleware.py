from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get("user_timezone")
        if tzname:
            timezone.activate(tzname)
        return self.get_response(request)
