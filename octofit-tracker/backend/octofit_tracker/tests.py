from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=10)
        self.workout = Workout.objects.create(user=self.user, name='Test Workout', description='desc')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=42)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')
    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')
    def test_activity(self):
        self.assertEqual(self.activity.type, 'Test Activity')
    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 42)
