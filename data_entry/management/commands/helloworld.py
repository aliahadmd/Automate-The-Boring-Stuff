from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This is a helloworld command"

    # print helloworld with python manage.py helloworld
    def handle(self, *args, **kwargs):
        # print hello world
        self.stdout.write("Hello World")
