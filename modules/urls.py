from django.urls import re_path
from modules import views

urlpatterns=[
    re_path(r'^user$', views.UserApi),
    re_path(r'^user/([0-9]+)$', views.UserApi),
    re_path(r'^template$', views.TemplatesAPI),
    re_path(r'^template/([0-9])/([0-9])$', views.TemplatesAPI)
]