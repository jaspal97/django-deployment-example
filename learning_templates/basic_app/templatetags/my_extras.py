from django import template

register=template.Library()

def cut(value,arg):
    """
        This cuts all arg from value
    """
    return value.replace(arg,'')

register.filter('cut',cut)
