from msilib.schema import Class
from attr import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    # Making the password dissapear maybe create other serializer!
    #     extra_kwargs = {
    #         'password':{
    #             'write_only':True
    #             }
    #     }

    # def create(self, validated_data):
    #     validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     instance.save()
    #     return instance


class UserSerializerNoPass(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    # Making the password dissapear maybe create other serializer!
        extra_kwargs = {
            'password':{
                'write_only':True
                }
        }

    def create(self, validated_data):
        validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance