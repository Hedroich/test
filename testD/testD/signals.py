from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from sig.models import Project
#
@receiver(post_save, sender=Project)
def project_log(sender, instance, created, **kwargs ):
    if created:
        print("Проект создан")

@receiver(post_delete, sender=Project)
def project_log(sender, instance, **kwargs):
    print("Проект удален")

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def new_user(created, **kwargs):
    print("Новый пользователь")