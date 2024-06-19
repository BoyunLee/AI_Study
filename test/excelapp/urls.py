from django.urls import path

from excelapp import views

urlpatterns = [
    ### http://127.0.0.1:8000/excel/
    path('', views.ExcelPage),
]
