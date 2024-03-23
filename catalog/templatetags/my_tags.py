from django import template

register = template.Library()


@register.filter
def get_image(img):
    if img:
        return f'/media/{img}'
    else:
        return '/static/no_photo.jpg'
