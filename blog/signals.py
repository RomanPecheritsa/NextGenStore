from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Article
from blog.utils import send_congratulation_email


@receiver(post_save, sender=Article)
def check_views_count(sender, instance, **kwargs):
    if instance.views_count == 100:
        send_congratulation_email(instance)
