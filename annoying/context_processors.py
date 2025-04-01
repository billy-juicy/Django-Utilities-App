from django.conf import settings

def rp_context(request):
    context_data = dict()
    context_data['STATIC_URL'] = settings.STATIC_URL
    return context_data
