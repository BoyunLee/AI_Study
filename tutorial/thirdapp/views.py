from django.shortcuts import render

def getIndexPage(request) :
    return render(
        request,
        "thirdapp/index.html",
        {}
    )