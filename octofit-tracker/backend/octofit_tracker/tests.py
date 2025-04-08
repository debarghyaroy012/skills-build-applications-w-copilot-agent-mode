from rest_framework.test import APITestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        response = self.client.post('/api/users/', {'email': 'test@example.com', 'name': 'Test User'})
        self.assertEqual(response.status_code, 201)

class TeamTests(APITestCase):
    def test_create_team(self):
        response = self.client.post('/api/teams/', {'name': 'Test Team', 'members': []})
        self.assertEqual(response.status_code, 201)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test@example.com', name='Test User')
        response = self.client.post('/api/activity/', {'user': user.id, 'type': 'Running', 'duration': 30})
        self.assertEqual(response.status_code, 201)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(email='test@example.com', name='Test User')
        response = self.client.post('/api/leaderboard/', {'user': user.id, 'score': 100})
        self.assertEqual(response.status_code, 201)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        response = self.client.post('/api/workouts/', {'name': 'Test Workout', 'description': 'Test Description'})
        self.assertEqual(response.status_code, 201)
