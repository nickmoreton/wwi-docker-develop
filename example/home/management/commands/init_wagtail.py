from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="The admin account username")
        parser.add_argument("password",type=str,help="The admin account password")
        parser.add_argument("email",type=str,help="The admin account email")
    
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            print('Creating account for %s (%s)' % (options["username"], options["email"]))
            admin = User.objects.create_superuser(email=options["email"], username=options["username"], password=options["password"])
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exists')
