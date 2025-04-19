from django import template

register = template.Library()

@register.filter
def get_column(article, column):
    if column == "price":
        price = article.get(column).get("value",'')
        if price == None:
            price=''
        currency = article.get(column).get("currency",'')
        if currency == None:
            currency=''
        return price+currency
    return article.get(column, '')