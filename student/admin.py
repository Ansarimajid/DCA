from django.contrib import admin
from .models import StudentInfo, CourseSubscription, PaymentProcess, LectureProgress

# Register your models here.
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('username','email_id','mobile_no','dob','address')
    list_per_page = 20
    search_fields = ('username','mobile_no','address')
    readonly_fields = ('username','email_id','mobile_no','dob','address')

class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('student','course','progress')
    list_per_page = 20
    search_fields = ('student','course')
    readonly_fields = ('payment_id','order_id','DateStamp',)
    list_filter = ('student','course','DateStamp')
    
    def save_model(self, request, obj, form, change):
        obj.update_progress()
        super().save_model(request, obj, form, change)
        
class LectureProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'lecture', 'completed')
    list_filter = ('completed', 'lecture__course')
    search_fields = ('student__username__username', 'lecture__title')

class PaymentProcessAdmin(admin.ModelAdmin):
    list_display = ('course','student','payment_status')
    list_filter = ('payment_status','course')

admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(CourseSubscription, CourseSubscriptionAdmin)
admin.site.register(PaymentProcess, PaymentProcessAdmin)
admin.site.register(LectureProgress, LectureProgressAdmin)
