"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

### include : 외부 모듈(파일)을 현재 파일에 포함시키기
# - 외부 코드를 포함시키는 기능
from django.urls import path, include

### 사용자의 페이지주소에 해당하는 처리함수는 모듈단위로 구성됩니다.
# - 해당 모듈 내에 함수로 정의되어 있습니다.
from mainapp import views as m_views

urlpatterns = [
    
    ### include 사용하기 ###############################
    
    # - 외부 각각의 app의 urls.py 파일을 생성하여 관리하고,
    # - config/urls.py에서 코드를 불러들여서(포함시켜서) 사용
    # - http://127.0.0.1:8000/first/ url은 
    #   무조건 firstapp의 urls.py에서 처리되도록함
    path('first/', include('firstapp.urls')),
    # - http://127.0.0.1:8000/second/
    path('second/', include('secondapp.urls')),
    # - http://127.0.0.1:8000/third/
    path('third/', include('thirdapp.urls')),
    # - http://127.0.0.1:8000/front/
    path('front/', include('frontapp.urls')),
    # - http://127.0.0.1:8000/mysql/
    path('mysql/', include('mysqlapp.urls')),
    
     
    
    ### include 사용안하기 ###############################
    
    ### http://127.0.0.1:8000/ 으로 요청이 들어오는 경우
    # - firstapp의 getIndexPage 호출하기
    path('', m_views.index),
    
    
    ### Django가 관리하는 관리자페이지 영역(고려 대상 아님)
    path('admin/', admin.site.urls),
]
