from django.http import JsonResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import User


@csrf_exempt
def user(request):
    if request.method =="GET":
        print("GET success")
        return HttpResponse("GET success")
    elif request.method =="POST":
        print("POST success")
        return HttpResponse("POST success")
    elif request.method =="PUT":
        print("PUT success")
        return HttpResponse("PUT success")
    elif request.method =="DELETE":
        print("DELETE success")
        return HttpResponse("DELETE success")

@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self,request,*args,**kwargs):
        user_id=kwargs.get("pk")
        print(user_id)
        if user_id:
            user_value=User.objects.filter(pk=user_id).values("username","password").first()
            print(user_value)
            if user_value:
                return JsonResponse({
                    "status":200,
                    "msg":"查询单个用户",
                    "results":user_value
                })
        else:
            user_list=User.objects.all().values("username","password")
            print(user_list)
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "msg": "查询所有用户",
                    "results": list(user_list),
                })
        return JsonResponse({
            "status": 500,
            "msg": "查询失败",
        })
    def post(self,request,*args,**kwargs):
        # print("POST success")
        # print(request.POST)
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user_object=User.objects.create(username=username,password=password)
            print("创建成功")
            return JsonResponse({
                "status":300,
                "msg":"创建成功",
                "result":{"username":user_object.username,"pwd":user_object.password}
            })
        except:
            return JsonResponse({
                "status": 500,
                "msg": "创建失败",
            })
        # return HttpResponse("成功")
    def put(self,request,*args,**kwargs):
        print("PUT success")
        return HttpResponse("PUT success")
    def delete(self,request,*args,**kwargs):
        print("DELETE success")
        return HttpResponse("DELETE success")
class UserAPIView(APIView):
    def get(self,request,*args,**kwargs):
        print(request.GET)
        print(request.query_params)
        return Response("DRF get success")
    def post(self,request,*args,**kwargs):
        # print("POST GET VIEW")
        print(request.POST)
        print(request.data)
        return Response("DRF post success")