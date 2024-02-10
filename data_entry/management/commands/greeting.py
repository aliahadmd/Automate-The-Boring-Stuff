from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This is a gretting command"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="User name")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        greeting = f"Hi, {name}. Good morning!"
        self.stdout.write(self.style.SUCCESS(greeting))
