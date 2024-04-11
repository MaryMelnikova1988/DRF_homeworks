from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from online_studing.models import Course, Subscription


@shared_task
def send_mail_about_update_course(course_id):
    course = Course.objects.get(pk=course_id)
    subs = Subscription.objects.all().filter(course=course)
    for sub in subs:
        send_mail(
            subject=f'{course.title}',
            message=f'В {course.title} появились обновления',
            recipient_list=[f'{sub.user.email}'],
            from_email=EMAIL_HOST_USER
        )