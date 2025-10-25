from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

# 
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, error_messages={
        'min_length': 'Le mot de passe doit contenir au moins 8 caractères.',
        'blank': 'Le mot de passe est requis.'
    })

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        read_only_fields = ('id',)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value

    def validate(self, data):
        if not data.get('email'):
            raise serializers.ValidationError({"email": "L'email est requis."})
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, error_messages={
        'blank': "L'email est requis.",
        'invalid': "Veuillez entrer un email valide."
    })
    password = serializers.CharField(write_only=True, required=True, error_messages={
        'blank': 'Le mot de passe est requis.'
    })

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise serializers.ValidationError({
                'non_field_errors': ['Email ou mot de passe incorrect.']
            })
        return {'user': user}