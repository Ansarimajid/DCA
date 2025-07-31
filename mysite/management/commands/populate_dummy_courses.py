from django.core.management.base import BaseCommand
from mysite.models import Course, Section, Lecture

class Command(BaseCommand):
    help = 'Populate the database with dummy courses and YouTube links'

    def handle(self, *args, **kwargs):
        courses_data = [
            {
                "title": "Python for Beginners",
                "description": "Learn Python from scratch.",
                "thumbnail_url": "https://dummyimage.com/300.png/09f/fff",
                "course_type": "FREE",
                "course_length": "10 hours",
                "course_price": 0,
                "sections": [
                    {
                        "title": "Introduction",
                        "lectures": [
                            {
                                "title": "Getting Started",
                                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Advanced JavaScript",
                "description": "Deep dive into JavaScript.",
                "thumbnail_url": "https://dummyimage.com/300.png/09a/fff",
                "course_type": "PAID",
                "course_length": "15 hours",
                "course_price": 50,
                "sections": [
                    {
                        "title": "Advanced Topics",
                        "lectures": [
                            {
                                "title": "Closures in JavaScript",
                                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Data Science with Python",
                "description": "Explore data handling, visualization, and more.",
                "thumbnail_url": "https://dummyimage.com/300.png/08f/fff",
                "course_type": "PAID",
                "course_length": "20 hours",
                "course_price": 100,
                "sections": [
                    {
                        "title": "Data Analysis",
                        "lectures": [
                            {
                                "title": "Introduction to Pandas",
                                "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            }
                        ]
                    }
                ]
            },
        ]

        for course_data in courses_data:
            course = Course.objects.create(
                title=course_data['title'],
                description=course_data['description'],
                thumbnail_url=course_data['thumbnail_url'],
                course_type=course_data['course_type'],
                course_length=course_data['course_length'],
                course_price=course_data['course_price'],
            )
            for section_data in course_data.get('sections', []):
                section = Section.objects.create(
                    title=section_data['title'],
                    course=course
                )
                for lecture_data in section_data.get('lectures', []):
                    Lecture.objects.create(
                        title=lecture_data['title'],
                        section=section,
                        video_url=lecture_data['video_url'],
                    )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
