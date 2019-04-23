from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from meiduo_mall.libs.captcha.captcha import captcha
from django.http import HttpResponse

# Create your views here.

class ImageCodeView(View):
    """生成图形验证码"""
    def get(self,request,uuid):
        print("haha")
        # 利用SDK 生成图形验证码 (唯一标识字符串, 图形验证内容字符串, 二进制图片数据)
        name,text,image = captcha.generate_captcha()

        # 创建redis连接对象,参数是别名
        redis_conn=get_redis_connection('verify_code')
        # 将图形验证码字符串存入到reids
        redis_conn.setex('img_%s'% uuid, 300, text)

        return HttpResponse(image,content_type='image/jpg')

