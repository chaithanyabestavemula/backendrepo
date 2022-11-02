from django.core.management.base import BaseCommand
from backend.models import vehicle

class Command(BaseCommand):
    help = 'adds into list'
    def add_arguments(self, parser):
       parser.add_argument('lp_number')
       parser.add_argument('wheelcount')
       parser.add_argument('manufacturer')
       parser.add_argument('model')
    def handle(self, *args, **options):
        members=vehicle(
            lp_number=options['lp_number'],
            wheelcount=options['wheelcount'],
            manufacturer=options['manufacturer'],
            model=options['model']

        )
        members.save()
        print("vehicle added")



