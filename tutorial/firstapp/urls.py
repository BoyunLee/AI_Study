from django.urls import path

from . import views

urlpatterns = [
    
    ### http://127.0.0.1:8000/first/
    path('', views.getIndexPage),
    
    ### http://127.0.0.1:8000/first/01_html/ 
    path('01_html/', views.htmlview01),

]
