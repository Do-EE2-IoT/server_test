from rest_framework import serializers
from .models import Course
class getAllCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id','title')


class CourseSerializer(serializers.Serializer):
    title1 = serializers.CharField(max_length=200)
    content1 = serializers.CharField(max_length = 200)
    price1 = serializers.IntegerField()
