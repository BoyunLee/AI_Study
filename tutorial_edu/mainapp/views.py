from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

### http://127.0.0.1:8000/
def index(request) :
    msg = "이 곳은 mainapp 페이지 입니다"
    # return HttpResponse(msg)
    
    ### render함수 : 사용자의 요청(request)과 Back-end 프로그램 변수들(딕셔너리{})을 이용해서
    #              : html에 넣는 작업을 수행합니다.
    return render(
        request,
        # html 페이지 위치 지정
        "mainapp/index.html",
        # html 페이지에 넣어줄 값들 정의(없으면 빈 딕셔너리로 처리)
        {}
    )