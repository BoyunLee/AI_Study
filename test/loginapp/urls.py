from django.urls import path

from loginapp import views

urlpatterns = [
    path('', views.LoginPage),
    
    ### http://127.0.0.1:8000/logincheck/
    path('logincheck/', views.LoginCheck),
    
]
