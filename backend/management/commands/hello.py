from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'disp hello'
    def add_arguments(self, parser):
       parser.add_argument('first')
       parser.add_argument('--option1')



    def handle(self, *args, **options):
        self.stdout.write("hello world")
        print(f'{ options["first"]} ' )
        print(f'{options["option1"]} ' )




