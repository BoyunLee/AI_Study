from django.urls import path

### 사용자의 페이지주소에 해당하는 처리함수는 모듈단위로 구성됩니다.
# - 해당 모듈 내에 함수로 정의되어 있습니다.
from . import views

urlpatterns = [
    
    ### http://127.0.0.1:8000/third/으로 요청이 들어오는 경우
    path('', views.index),
]
