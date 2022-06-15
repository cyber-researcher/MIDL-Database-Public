from pipes import Template
from rest_framework import serializers
from modules.models import User, Templates

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model= User
        fields=('UserId','UserName')

class TemplatesSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Templates
        fields=('Id', 'TemplateUserId','TemplateName', 'Routes', 'Template')