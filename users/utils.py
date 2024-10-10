from django.core.mail import send_mail
from string import ascii_letters, digits
from random import choices

from nextgenstore.settings import EMAIL_HOST_USER


def send_email_confirm(url, email):
    send_mail(
        subject="Подтвержение регистрации на сайте NextGen Store",
        message=f"Для подтверждения регистрации, перейдите по ссылке {url}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
    )


def send_email_reset_password(password, email):
    send_mail(
        subject="Сброс пароля на сайте NextGen Store",
        message=f"Новый пароль {password}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
    )


def generate_random_password():
    data = ascii_letters + digits
    return "".join(choices(data, k=8))
