from pipes import Template
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from modules.models import User, Templates
from modules.serializers import UserSerializer, TemplatesSerializer
# Create your views here.

@csrf_exempt
def UserApi(request, id = 0):
    if request.method=='GETALL':
        userId = User.objects.all()
        userId_serializer = UserSerializer(userId, many = True)
        return JsonResponse(userId_serializer.data, safe=False)

    elif request.method=='GETSPECIFIC':
        userId = User.objects.get(UserId = id)
        userId_serializer = UserSerializer(userId, many = False)
        return JsonResponse(userId_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        userId_serializer = UserSerializer(data=user_data)
        if userId_serializer.is_valid():
            userId_serializer.save()
            return JsonResponse('User Added Successfully,', safe = False)
        return JsonResponse('Failed to add User', safe = False)

    elif request.method =='PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(UserId=user_data['UserId'])
        userId_serializer = UserSerializer(user, data=user_data)
        if userId_serializer.is_valid():
            userId_serializer.save()
            return JsonResponse('User updated', safe=False)
        return JsonResponse('Failed Updated User', safe=False)

    elif request.method == 'DELETE':
        user = User.objects.get(UserId=id)
        user.delete()
        return JsonResponse('Delete Successful')
    
@csrf_exempt
def TemplatesAPI(request, id = 0, userid= 0):
    if request.method=='GETALL':
        print('hello')
        templateId = Templates.objects.all()
        templateId_serializer = TemplatesSerializer(templateId, many = True)
        return JsonResponse(templateId_serializer.data, safe=False)

    elif request.method=='GET':
        userId = Templates.objects.get(TemplateUserId = userid)
        templateId = Templates.objects.get(Id = id)
        templateId_serializer = TemplatesSerializer(templateId, many = False)
        return JsonResponse(templateId_serializer.data, safe=False)
        
    elif request.method == 'POST':
        template_data = JSONParser().parse(request)
        templateId_serializer = TemplatesSerializer(data=template_data)
        if templateId_serializer.is_valid():
            templateId_serializer.save()
            return JsonResponse('User Added Successfully,', safe = False)
        return JsonResponse('Failed to add Template', safe = False)

    elif request.method =='PUT':
        template_data = JSONParser().parse(request)
        template = User.objects.get(id=template_data['UserId'])
        template_serializer = TemplatesSerializer(template, data=template_data)
        if template_serializer.is_valid():
            template_serializer.save()
            return JsonResponse('User updated', safe=False)
        return JsonResponse('Failed Updated User', safe=False)

    elif request.method == 'DELETE':
        template = User.objects.get(id=id)
        template.delete()
        return JsonResponse('Delete Successful')
    

