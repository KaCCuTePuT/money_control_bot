from celery.schedules import crontab
from django.core.mail import EmailMessage

from config.celery_settings import app


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    """Периодическая отправка на почту"""
    sender.add_periodic_task(
        crontab(hour=9, minute=13, day_of_month=12),
        send_report_on_email.s(),
    )


@app.task
def send_report_on_email(month: int, report: str):
    """Отправка отчета на почту"""
    message = EmailMessage(
        f'Отчет за {month} месяц',
        report,
        'nopro.ru@gmail.com',
        ['nopro.ru@gmail.com'],
    )
    message.content_subtype = 'html'
    message.attach_file('report_common.pdf')
    message.send()

