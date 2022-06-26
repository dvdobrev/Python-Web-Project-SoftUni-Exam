# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from poker_app.web.tasks import send_email_when_user_is_created
#
# UserModel = get_user_model()
#
#
# @receiver(post_save, sender=UserModel)
# def user_created(instance, created, *args, **kwargs):
#     if not created:
#         return
#
#     send_email_when_user_is_created.delay(instance.pk)
