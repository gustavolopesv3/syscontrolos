from django import template

register = template.library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='filtre')
def get_item(dictionary, key):
    return dictionary.get(key)
