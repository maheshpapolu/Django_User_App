from celery import shared_task
from django.core.mail import send_mail


# from python_notes import settings.dev

@shared_task()
def send_email(token, to, name):
    print(token)
    send_mail(from_email='maheshnaidu9666@gmail.com', recipient_list=[to],
              message="Hy {}\nWelcome to python_notes,Thanks for installing our service\nYour Activation url = "
                      "http://127.0.0.1:8000/user/validate/{}".format(name, token),
              subject="Link for Your Registration", fail_silently=False,)
