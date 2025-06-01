from django.urls import re_path

from . import views

# 发短信
urlpatterns = [
    re_path(r'^smscodes/(?P<mobile>1[3-9]\d{9})$', views.SMSCodeView.as_view())
]
