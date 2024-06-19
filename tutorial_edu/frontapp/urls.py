from django.urls import path

### 사용자의 페이지주소에 해당하는 처리함수는 모듈단위로 구성됩니다.
# - 해당 모듈 내에 함수로 정의되어 있습니다.
from . import views

urlpatterns = [
    ### http://127.0.0.1:8000/front/
    path('', views.index),
    
    ### http://127.0.0.1:8000/front/01_html/
    path('01_html/', views.htmlView01),
    
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
        
    ### http://127.0.0.1:8000/front/12_div/
    path('12_div/', views.divView12),
        
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
    path('16_checkBoxView/', views.checkBoxView16),
    ### http://127.0.0.1:8000/front/17_checkBox/
    path('17_checkBox/', views.checkBox17),
        
    ### http://127.0.0.1:8000/front/18_selectBoxView/
    path('18_selectBoxView/', views.selectBoxView18),
    ### http://127.0.0.1:8000/front/19_selectBox/
    path('19_selectBox/', views.selectBox19),
    
    
    ############## [레이아웃 분리 : include] #############
    ### http://127.0.0.1:8000/front/20_include/
    path('20_include/', views.includeView),
    
    
    ############## [레이아웃 분리 : extend] #############
    ### http://127.0.0.1:8000/front/21_extend_layout/
    path('21_extend_layout/', views.extendLayoutView),
    ### http://127.0.0.1:8000/front/22_section/
    path('22_section/', views.extendSection),
    ### http://127.0.0.1:8000/front/23_table/
    path('23_table/', views.extendTable),
    
    ############## [Bootstrap] #############
    ### http://127.0.0.1:8000/front/01_bootstrap/
    path('01_bootstrap/', views.bootstrap01),
    ### http://127.0.0.1:8000/front/02_bootstrap_table/
    path('02_bootstrap_table/', views.bootstrap_table02),
    
    ############## [앤스콤 데이터 시각화] #############
    ### http://127.0.0.1:8000/front/data_view/
    path('data_view/', views.createAnscombe_Image),
    
    ############## [모델을 이용하여 예측하기] #############
    ### http://127.0.0.1:8000/front/ml_predict/
    path('ml_predict/', views.getML_Predict),
]
