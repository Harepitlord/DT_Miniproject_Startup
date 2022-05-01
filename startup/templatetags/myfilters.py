from django import template

register = template.library()


@register.filter('addCSSClass')
def addCSSClass(value, arg: str):
    return value.as_widget(attrs={'class': arg})
