from celery import shared_task
from dateutil.relativedelta import *
from django.utils import timezone

from users.models import User


# @shared_task
# def deactivate_user():
#     month_ago = datetime.now().date() - relativedelta(months=1)
#     users = User.objects.filter(is_active=True)
#     for user in users:
#         if user.last_login is not None:
#             if user.last_login.date() < month_ago:
#                 user.is_active = False
#                 user.save()
#                 print(f"{user} был деактивирован")


@shared_task
def deactivate_user():
    month_ago = timezone.now() - relativedelta(months=1)
    users = User.objects.filter(is_active=True, last_login__lte=month_ago)
    updated_users_count = users.update(is_active=False)
    if updated_users_count:
        print(f'{updated_users_count} пользователей было деактивировано')
