from django.conf import settings

def auto_logout_delay(request):
    return {
        'AUTO_LOGOUT_DELAY': settings.AUTO_LOGOUT_DELAY,
    }
