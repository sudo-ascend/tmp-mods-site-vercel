from django import template

register = template.Library()

@register.filter
def get_path_part(value, index):
    parts = value.strip('/').split('/')
    if index < len(parts):
        return parts[index]
    else:
        return 'main'