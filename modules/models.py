from tkinter import CASCADE
from django.db import models
from django.forms import JSONField
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    UserId = models.AutoField(
        'user_id',
        primary_key=True
    )
    UserName = models.CharField(
        max_length=255
    )

    def __str__(self):
        return str(self.UserId)


class Templates(models.Model):
    Id = models.AutoField(
        'Id',
        primary_key=True
    )
    TemplateUserId = models.ForeignKey(
        User,
        verbose_name='template_user_id',
        on_delete=models.CASCADE
        )
    TemplateName = models.CharField(
        'template_name',
        max_length=255
    )

    Template = models.JSONField()
    
    Routes = models.CharField(
         'routes',
        max_length=255
    )
    def __str__(self):
        return str(self.Id)
#need to fix the db


# Create your models here.
