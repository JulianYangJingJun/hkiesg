from django import template
from menus.models import MainMenu
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag(takes_context=True)
def get_main_menu(context):
    current_language = get_language()
    menu = MainMenu.objects.first()
    return {
        'menu': menu,
        'current_language': current_language
    }