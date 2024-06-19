from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


### http://127.0.0.1:8000/first/
def index(request): 
    return render(
        request, 
        "firstapp/index.html",
        {}
    )

### http://127.0.0.1:8000/first/01_html/
def htmlview01(request) :
    return render(
        request,
        "firstapp/front/01_html.html",
        {}
    )

















