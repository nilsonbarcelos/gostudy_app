from django import template

# create a instance template library in order to create a template filter
register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})