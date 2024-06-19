from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


### http://127.0.0.1:8000/ 처리
def getIndexPage(request) :
    # msg = "이곳은 mainapp 페이지 입니다."
    # return HttpResponse(msg)
    
    return render(
        request,
        # html 페이지 위치 지정
        "mainapp/index.html",
        # html 페이지에 넣어줄 값들 정의(없으면 빈 딕셔너리로 처리)
        {}
    )