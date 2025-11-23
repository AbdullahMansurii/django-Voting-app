from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from polls.models import Poll, Choice


class Command(BaseCommand):
    """
    Management command to create sample polls for testing.
    Run with: python manage.py create_sample_polls
    """
    help = 'Creates sample polls with choices for testing the voting app'

    def handle(self, *args, **options):
        """Main method that runs when command is executed"""
        
        # Clear existing polls (optional - comment out if you want to keep existing data)
        Poll.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared existing polls'))
        
        # Create Active Poll 1
        poll1 = Poll.objects.create(
            title="What's your favorite programming language?",
            question="Which programming language do you enjoy working with the most?",
            is_active=True,
            end_date=timezone.now() + timedelta(days=7)
        )
        Choice.objects.create(poll=poll1, choice_text="Python")
        Choice.objects.create(poll=poll1, choice_text="JavaScript")
        Choice.objects.create(poll=poll1, choice_text="Java")
        Choice.objects.create(poll=poll1, choice_text="C++")
        Choice.objects.create(poll=poll1, choice_text="Other")
        self.stdout.write(self.style.SUCCESS(f'Created poll: {poll1.title}'))
        
        # Create Active Poll 2
        poll2 = Poll.objects.create(
            title="Best framework for web development?",
            question="Which web framework do you prefer for building modern web applications?",
            is_active=True,
            end_date=timezone.now() + timedelta(days=5)
        )
        Choice.objects.create(poll=poll2, choice_text="Django")
        Choice.objects.create(poll=poll2, choice_text="Flask")
        Choice.objects.create(poll=poll2, choice_text="React")
        Choice.objects.create(poll=poll2, choice_text="Vue.js")
        Choice.objects.create(poll=poll2, choice_text="Angular")
        self.stdout.write(self.style.SUCCESS(f'Created poll: {poll2.title}'))
        
        # Create Active Poll 3
        poll3 = Poll.objects.create(
            title="Preferred development environment?",
            question="What's your go-to development environment or IDE?",
            is_active=True,
            end_date=timezone.now() + timedelta(days=10)
        )
        Choice.objects.create(poll=poll3, choice_text="VS Code")
        Choice.objects.create(poll=poll3, choice_text="PyCharm")
        Choice.objects.create(poll=poll3, choice_text="Sublime Text")
        Choice.objects.create(poll=poll3, choice_text="Vim/Neovim")
        Choice.objects.create(poll=poll3, choice_text="Other")
        self.stdout.write(self.style.SUCCESS(f'Created poll: {poll3.title}'))
        
        # Create Past Poll (for testing past polls view)
        poll4 = Poll.objects.create(
            title="Favorite database system?",
            question="Which database system do you prefer for your projects?",
            is_active=False,
            end_date=timezone.now() - timedelta(days=5)
        )
        Choice.objects.create(poll=poll4, choice_text="PostgreSQL", votes=45)
        Choice.objects.create(poll=poll4, choice_text="MySQL", votes=30)
        Choice.objects.create(poll=poll4, choice_text="SQLite", votes=15)
        Choice.objects.create(poll=poll4, choice_text="MongoDB", votes=25)
        Choice.objects.create(poll=poll4, choice_text="Other", votes=10)
        self.stdout.write(self.style.SUCCESS(f'Created past poll: {poll4.title}'))
        
        self.stdout.write(self.style.SUCCESS('\nSuccessfully created sample polls!'))
        self.stdout.write(self.style.WARNING('You can now run: python manage.py runserver'))


