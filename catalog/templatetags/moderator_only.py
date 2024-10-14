from django import template

register = template.Library()


@register.filter(name="has_required_perms")
def has_required_perms(user):

    required_perms = [
        "catalog.can_unpublish_product",
        "catalog.can_change_description",
        "catalog.can_change_category",
    ]
    return user.has_perms(required_perms)
