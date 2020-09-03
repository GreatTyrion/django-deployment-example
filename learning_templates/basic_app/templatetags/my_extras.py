from django import template

register = template.Library()


@register.filter(name='cut_string')
def self_made_cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, "")


# register.filter('cut_string', self_made_cut)
