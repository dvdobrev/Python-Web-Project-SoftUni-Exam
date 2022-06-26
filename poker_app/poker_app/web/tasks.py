# from celery import shared_task
# from django.contrib.auth import get_user_model
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
#
# UserModel = get_user_model()
#
#
# @shared_task
# def send_email_when_user_is_created(user_pk):
#     user = UserModel.objects.get(pk=user_pk)
#
#     send_mail(
#         'Hello You did it!',
#         'Hi Dorbiiiii',
#         'django_dobri@abv.bg',
#         'salmokalte@vusra.com',
#     )

# context = {
#     'name': 'Dobri',
# }
# message = render_to_string('404.html', context)

# message,
