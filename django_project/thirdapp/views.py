from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

### http://127.0.0.1:8000/ 처리
def getIndexPage(request) :
    return render(
        request,
        "thirdapp/index.html",
        {}
    )