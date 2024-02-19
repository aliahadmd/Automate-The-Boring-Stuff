from django.core.management.base import BaseCommand

from data_entry.models import Student


class Command(BaseCommand):
    help = "Insert data into the database"

    def handle(self, *args, **kwargs):
        students = [
            {"roll_no": 1, "name": "Ali", "age": 21},
            {"roll_no": 2, "name": "Bob", "age": 22},
            {"roll_no": 3, "name": "Charlie", "age": 23},
            {"roll_no": 4, "name": "David", "age": 24},
            {"roll_no": 5, "name": "Jhon", "age": 26},
        ]

        for student in students:
            roll_no = student["roll_no"]
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(
                    roll_no=student["roll_no"], name=student["name"], age=student["age"]
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Record with roll no {roll_no} already exists")
                )

        self.stdout.write(self.style.SUCCESS("Successfully inserted data"))
