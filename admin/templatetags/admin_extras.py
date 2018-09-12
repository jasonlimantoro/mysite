from django import template

register = template.Library()


@register.simple_tag
def query_filter(obj, **kwargs):
    return obj.filter(**kwargs)


@register.simple_tag
def count_filter(obj, **kwargs):
    return query_filter(obj, **kwargs).count()

