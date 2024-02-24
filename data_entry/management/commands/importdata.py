from django.core.management.base import BaseCommand, CommandError
# from data_entry.models import Student
from django.apps import apps
import csv

# command will be - python manage.py importdata file_path model_name

class Command(BaseCommand):
    help = "Import data from a csv file"
    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="The path to the csv file")
        parser.add_argument("model_name", type=str, help='Name of the model')




    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs ['model_name']

        # serach for the model across all installed apps
        for app_config in apps.get_app_configs():

            #try to search for the model
            try:
                model =apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found
            except LookupError:
                continue
        
        if not model:
            raise CommandError(f'Model"{model_name}" not found in any app!' )


        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS("Data imported from csv successfully"))


