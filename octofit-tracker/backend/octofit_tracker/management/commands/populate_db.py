from django.core.management.base import BaseCommand
from fitness_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(email='zerocool@mhigh.edu', name='Elliot Alderson'),
            User(email='crashoverride@hmhigh.edu', name='Dade Murphy'),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token'),
        ]
        # Save users to the database first
        for user in users:
            user.save()

        # Update teams to store user IDs in the members field
        teams = [
            Team(name='Blue Team', members=[str(users[0].id), str(users[1].id)]),
            Team(name='Gold Team', members=[str(users[2].id), str(users[3].id), str(users[4].id)]),
        ]
        for team in teams:
            team.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60),
            Activity(user=users[1], type='Crossfit', duration=120),
            Activity(user=users[2], type='Running', duration=90),
            Activity(user=users[3], type='Strength', duration=30),
            Activity(user=users[4], type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100),
            Leaderboard(user=users[1], score=90),
            Leaderboard(user=users[2], score=95),
            Leaderboard(user=users[3], score=85),
            Leaderboard(user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
