from django import template
register = template.Library()

@register.filter
def dictKey(mapping, key):
  return mapping.get(key, '')

