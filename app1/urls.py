from django.urls import path
from app1 import views
urlpatterns=[
    path("user/",views.user),
    path("users/",views.UserView.as_view()),
    path("users/<str:pk>/",views.UserView.as_view()),
    path("api_user/",views.UserAPIView.as_view()),
]