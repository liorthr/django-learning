from django import template
from translate import Translator
# from django.template.defaultfilters import stringfilter

register = template.Library()
tarnslator = Translator(to_lang='fr')
# @register.filter
# @stringfilter
# def first_char(value):
#     return value[0]
@register.simple_tag
def hello_world(value):
    return tarnslator.translate(value)