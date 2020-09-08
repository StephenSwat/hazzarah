from django import template


register = template.Library()


@register.filter
def gold(value):
    return value // 10000


@register.filter
def silver(value):
    return (value // 100) % 100


@register.filter
def copper(value):
    return value % 100