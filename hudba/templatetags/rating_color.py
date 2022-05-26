from django import template
from django.utils.safestring import SafeString

register = template.Library()


@register.filter
def set_color(rating):

    if type(rating) is SafeString:
        rating = int(rating)

    if 80 <= rating <= 100:
        badge_class = 'bg-success'
    elif 60 <= rating < 80:
        badge_class = 'bg-primary'
    elif 40 <= rating < 60:
        badge_class = 'bg-warning text-dark'
    elif 20 <= rating < 40:
        badge_class = 'bg-danger'
    else:
        badge_class = "bg-dark text-white"

    return badge_class

