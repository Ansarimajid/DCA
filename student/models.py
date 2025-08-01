from django.db import models
from django.contrib.auth.models import User
from mysite.models import Course, Lecture
from django.utils.timezone import now

# Create your models here.
class StudentInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email_id = models.EmailField(default="-")
    mobile_no = models.CharField(max_length=12)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.username.email} - {self.mobile_no}"

class LectureProgress(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class CourseSubscription(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    DateStamp = models.DateTimeField(default=now)
    progress = models.CharField(default="0 %", max_length=10)
    payment_id = models.CharField(max_length=50, default="-")
    order_id = models.CharField(max_length=50, default="-")

    def calculate_progress(self):
        total_lectures = Lecture.objects.filter(course=self.course).count()
        if total_lectures == 0:
            return "0 %"
        completed_lectures = LectureProgress.objects.filter(
            student=self.student, 
            lecture__course=self.course,
            completed=True
        ).count()
        percentage = round((completed_lectures / total_lectures) * 100)
        return f"{percentage} %"
    
    def update_progress(self):
        self.progress = self.calculate_progress()
        self.save()

    def __str__(self):
        return f"{self.student.username} ==== {self.course}"

class PaymentProcess(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50, default="-")
    payment_status = models.BooleanField(default=False)
    datestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.course} - {self.order_id} - {self.payment_status}"
    