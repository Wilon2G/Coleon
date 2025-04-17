from django import template

register = template.Library()

@register.filter
def get_column(article, column):
    return article.get(column, '')