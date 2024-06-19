from django.urls import path

from . import views

urlpatterns = [
    ### http://127.0.0.1:8000/front/
    path('', views.getIndexPage),
    
    ### http://127.0.0.1:8000/front/01_html/
    path('01_html/', views.htmlview01),
    
    ### http://127.0.0.1:8000/front/02_link/
    path('02_link/', views.linkView),
    
    ### http://127.0.0.1:8000/front/03_css/
    path('03_css/', views.cssView03),
    
    ### http://127.0.0.1:8000/front/04_css/
    path('04_css/', views.cssView04),
    
    ### http://127.0.0.1:8000/front/05_css/
    path('05_css/', views.cssView05),
    
    ### http://127.0.0.1:8000/front/06_css/
    path('06_css/', views.cssView06),
    
    ### http://127.0.0.1:8000/front/07_table/
    path('07_table/', views.tableView07),

    ### http://127.0.0.1:8000/front/08_table/
    path('08_table/', views.tableView08),
    
    ### http://127.0.0.1:8000/front/09_table/
    path('09_table/', views.tableView09),
    
    ### http://127.0.0.1:8000/front/10_ul/
    path('10_ul/', views.ulView10),
    
    ### http://127.0.0.1:8000/front/11_div/
    path('11_div/', views.divView11),
    
    ### http://127.0.0.1:8000/front/13_jsInputForm/
    path('13_jsInputForm/', views.jsInputFormView),
    
    ### http://127.0.0.1:8000/front/14_jsInputCheck/
    path('14_jsInputCheck/', views.jsInputCheck),
    
    ### http://127.0.0.1:8000/front/14_radioView/
    path('14_radioView/', views.radioView14),
    
    ### http://127.0.0.1:8000/front/15_radio/
    path('15_radio/', views.radio),
    
    ### http://127.0.0.1:8000/front/15_radioView/
    path('15_radioView/', views.radioView15),
    
    ### http://127.0.0.1:8000/front/16_radio/
    path('16_radio/', views.radio2),
    
    ### http://127.0.0.1:8000/front/16_checkBoxView/
    path('16_checkBoxView/', views.checkBox16),
    
    ### http://127.0.0.1:8000/front/17_checkBox/
    path('17_checkBox/', views.checkBox17),
    
    ### http://127.0.0.1:8000/front/18_selectBoxView/
    path('18_selectBoxView/', views.selectBoxView18),
    
    ### http://127.0.0.1:8000/front/19_selectBox/
    path('19_selectBox/', views.selectBox19),

]
