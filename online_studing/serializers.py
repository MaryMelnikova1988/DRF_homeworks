from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from online_studing.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)


    def get_lessons_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'

class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all())

    class Meta:
        model = Course
        fields = '__all__'
        # fields = ("title", "course", )


