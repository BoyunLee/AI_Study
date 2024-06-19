from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

### http://127.0.0.1:8000/index4/ 처리
def getIndex4(request) :
    msg = "이곳은 secondapp의 index4 페이지 입니다."
    return HttpResponse(msg)

### http://127.0.0.1:8000/ 처리
def getIndexPage(request) :
    # msg = "이곳은 secondapp의 index 페이지 입니다."
    # return HttpResponse(msg)
    return render(
        request,
        "secondapp/index.html",
        {}
    )