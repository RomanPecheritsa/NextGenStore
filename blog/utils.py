from django.core.mail import send_mail
from django.conf import settings


def send_congratulation_email(article):
    """
    Sends a congratulatory email to the author of the article when it reaches 100 views.
    """
    subject = "Поздравляем с достижением!"
    message = f'Ваша статья "{article.title}" достигла 100 просмотров!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ["pecheritsa.roman@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)
