from django.urls import path


### 사용자의 페이지주소에 해당하는 처리함수는 모듈단위로 구성됩니다.
# 해당 모듈 내에 함수로 정의되어 있습니다.
from . import views


urlpatterns = [
    
    ### 사용자요청 서버주소 + 페이지주소 : http://127.0.0.1:8000/second/
    # secondapp 호출
    path('', views.getIndexPage),
    
    ### http://127.0.0.1:8000/second/index4/ 으로 요청이 들어오는 경우
    # secondapp 호출
    path('index4/', views.getIndex4),
    
    ### http://127.0.0.1:8000/second/index5/ 으로 요청이 들어오는 경우
    # secondapp 호출
    path('index5/', views.getIndexPage),
    
]
