from django.core.management.base import BaseCommand

from data_entry.models import Student


class Command(BaseCommand):
    help = "Insert data into the database"

    students = [
        {"roll_no": 1, "name": "Ali", "age": 21},
        {"roll_no": 2, "name": "Bob", "age": 22},
        {"roll_no": 3, "name": "Charlie", "age": 23},
        {"roll_no": 4, "name": "David", "age": 24},
    ]

    for student in students:

        Student.objects.create(
            roll_no=student["roll_no"], name=student["name"], age=student["age"]
        )

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Successfully inserted data"))
