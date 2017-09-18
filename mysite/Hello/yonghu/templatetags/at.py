import json

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def at(list, num):
    obj = list.split(',')
    obj[0] = obj[0][1:]
    obj[-1] = obj[-1][:-1]
    return int(obj[num - 1])
