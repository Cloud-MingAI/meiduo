from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class SMSCodeView(APIView):
    """短信验证码"""

    def get(self, request, mobile):
        # 1. 生成验证码
        # 2. 创建redis连接对象
        # 3. 验证码存到redis
        # 4. 容联云通讯发送验证码
        pass
