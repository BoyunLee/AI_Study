from django.urls import path


### 사용자의 페이지주소에 해당하는 처리함수는 모듈단위로 구성됩니다.
# 해당 모듈 내에 함수로 정의되어 있습니다.
from . import views


urlpatterns = [

    ### 사용자요청 서버주소 + 페이지주소 : http://127.0.0.1:8000/first/
    # firstapp 호출
    path('', views.getIndexPage),
    
    ### 사용자요청 서버주소 + 페이지주소 : http://127.0.0.1:8000/first/index/
    # firstapp 호출
    path('index/', views.getIndexPage),
    
    ### http://127.0.0.1:8000/first/index2/ 으로 요청이 들어오는 경우
    # ffirstapp 호출
    path('index2/', views.getIndexPage),
    
    ### http://127.0.0.1:8000/first/index3/ 으로 요청이 들어오는 경우
    # firstapp 호출
    path('index3/', views.getIndex3),
    
]
