from datetime import datetime

from celery import shared_task
from dateutil.relativedelta import *

from users.models import User


@shared_task
def deactivate_user():
    month_ago = datetime.now().date() - relativedelta(months=1)
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login is not None:
            if user.last_login.date() < month_ago:
                user.is_active = False
                user.save()
                print(f"{user} был деактивирован")
