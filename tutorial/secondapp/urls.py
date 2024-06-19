from django.urls import path

from . import views

urlpatterns = [
    path('', views.getIndexPage),
    
    path('login/', views.LoginPage),
    
    ### http://127.0.0.1:8000/second/logincheck/
    path('logincheck/', views.LoginCheck),

]
