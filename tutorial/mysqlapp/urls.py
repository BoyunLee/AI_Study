from django.urls import path

from . import views

urlpatterns = [
    
    ### http://127.0.0.1:8000/mysql/
    path('', views.index),
    
    ### http://127.0.0.1:8000/mysql/mem_list
    path('mem_list/', views.getMenberList),
    
    ### http://127.0.0.1:8000/mysql/mem_view
    path('mem_view/', views.getMenberView),
    
    ### http://127.0.0.1:8000/mysql/mem_update_view
    path('mem_update_view/', views.getMenberUpdateView),
    
    ### http://127.0.0.1:8000/mysql/mem_update
    path('mem_update/', views.getMenberUpdate),

]
