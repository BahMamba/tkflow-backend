from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Le titre doit contenir au moins 3 caractères.")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("La description ne peut pas être vide.")
        return value