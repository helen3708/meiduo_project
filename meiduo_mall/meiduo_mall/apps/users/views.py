from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseForbidden
import re

# Create your views here.

class RegisteView(View):
    """注册"""
    def get(self,request):
        """提供注册页面"""
        return render(request,'register.html')

    def post(self,request):
        """用户注册功能"""

        # 接收前端传入的表单数据: username, password, password2, mobile, sms_code, allow
        username = request.POST.get('username')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        mobile=request.POST.get('mobile')
        sms_code= request.POST.get('sms_code')
        allow=request.POST.get('allow')

        # 校验前端传入的参数是否齐全
        if all([username,password,password2,mobile,sms_code,allow]) is False:
            return HttpResponseForbidden("缺少必传参数")

        # 校验数据前端传入数据是否符合要求
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$',username):
            return HttpResponseForbidden('请输入5-20个字符的用户名')
        if not re.match(r'^[0-9a-zA-Z]{8-20}$',password):
            return HttpResponseForbidden('请输入8-20位的密码')
        if password != password2:
            return HttpResponseForbidden('输入的密码两次不一致')
        if not re.match(r'^1[3-9]\d{9}$',mobile):
            return HttpResponseForbidden('您输入的手机号格式不正确')

        # TODO 短信验证码校验后期再补充


