from django import template

register = template.Library()


@register.filter
def preview_url(product):

    if product.preview:
        return product.preview.url
    return ""
