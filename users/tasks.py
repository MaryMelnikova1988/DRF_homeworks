from datetime import datetime

from celery import shared_task

from users.models import User


@shared_task
def deactivate_user():
    date_x = datetime.now() - datetime.timedelta(days=30)
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login < date_x:
            user.is_active = False
            user.save()
            print(f"{user} был деактивирован")
