from asyncore import write
from .models import Todo
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['id','task','status']

class RegisterUserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name','password2']
        
        extra_Kwargs={
            'first_name':{"required":True},
            'last_name':{"required":True}
        }
    def validate(self, data):
        if data.get('password') != data.get('password2'):

            raise serializers.ValidationError("Password did not match")

        return data
    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password=validated_data['password']
        user.is_staff=True
        user.is_active=True
        user.save()
        return user