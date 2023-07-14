from django import template
from django.template.defaultfilters import stringfilter



register =template.Library()


@register.filter(name="addcent")
def addcent(value):
    return value + 100

@register.filter(name='couper')
def couper(value, arg):

    return value.replace(arg, 'ooo')


@register.filter(name='miniscule')
@stringfilter
def miniscule(value):
    return value.upper()