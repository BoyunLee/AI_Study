from django.shortcuts import render

# Create your views here.
### http://127.0.0.1:8000/third/
def index(request) :
    return render(
        request,
        "thirdapp/index.html",
        {}
    )