from django.contrib import admin

from online_studing.models import Course, Lesson


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'preview', 'description',)
    list_filter = ('title',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'preview', 'description',)
    list_filter = ('title',)