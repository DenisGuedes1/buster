from rest_framework import serializers
from .models import User
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(required=False, default=False)
    is_superuser = serializers.BooleanField(read_only=True, source='user.is_superuser')

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)

        error={}

        if email and User.objects.filter(email=email):
            error['email'] = ['email already registered']

        if username and User.objects.filter(username=username):
           error['username'] = ['Username already taken']

        if error:
            raise serializers.ValidationError(error)       

        return data

    # def create(self, validated_data):
    #     is_employee = validated_data.pop('is_employee', False)
    #     user = User.objects.create_user(**validated_data)
    #     user.is_employee = is_employee
    #     if is_employee:
    #         user.is_superuser = is_employee
    #         user.is_employee
          
         
    #         user.save()
    #     return user
    
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     if instance.is_employee:
    #         rep['is_superuser'] = True
    #     return rep
    def create(self, validate_data):
        if validate_data["is_employee"]:
            return User.objects.create_superuser(**validate_data)
        return User.objects.create_user(**validate_data)