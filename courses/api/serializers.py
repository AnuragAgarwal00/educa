from rest_framework import serializers
from ..models import Subject, Course, Module, Content

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'subject', 'modules', 'title', 'slug', 'over_view', 'owner', 'created', ] 

class CourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = []


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)
    class Meta:
        model = Content
        fields = ['item', 'order']


class ModuleWithContentSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)
    class Meta:
        model = Module
        fields = ['title', 'description', 'order', 'contents']


class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'subject', 'slug', 'over_view', 'created', 'modules']
