from django.core.management.base import BaseCommand
from student.models import CourseSubscription

class Command(BaseCommand):
    help = 'Update progress for all course subscriptions'

    def handle(self, *args, **options):
        subscriptions = CourseSubscription.objects.all()
        updated_count = 0
        
        for subscription in subscriptions:
            old_progress = subscription.progress
            subscription.update_progress()
            new_progress = subscription.progress
            
            if old_progress != new_progress:
                updated_count += 1
                self.stdout.write(
                    f'Updated {subscription.student.username.username} - {subscription.course.title}: {old_progress} -> {new_progress}'
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {updated_count} course subscriptions')
        )
