from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data individually to avoid Djongo ObjectIdField bulk delete issue
        for model in [app_models.User, app_models.Team, app_models.Activity, app_models.Leaderboard, app_models.Workout]:
            for obj in model.objects.all():
                pk = getattr(obj, 'id', None)
                if pk is not None:
                    try:
                        obj.delete()
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f"Could not delete {model.__name__} object: {e}"))

        # Create teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create users
        users = [
            app_models.User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            app_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            app_models.User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            app_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        for user in users:
            app_models.Activity.objects.create(user=user, type='Running', duration=30)
            app_models.Activity.objects.create(user=user, type='Cycling', duration=45)

        # Create workouts
        for user in users:
            app_models.Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session')

        # Create leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
