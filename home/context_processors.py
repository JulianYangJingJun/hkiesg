from home.models import Logo

def logo_context(request):
    try:
        site_logo = Logo.objects.first()
    except Logo.DoesNotExist:
        site_logo = None
    return {
        'site_logo': site_logo
    } 