from django.shortcuts import render

def getIndexPage(request) :
    return render(
        request,
        "firstapp/index.html",
        {}
    )
    
def htmlview01(request) :
    return render(
        request,
        "firstapp/front/01_html.html",
        {}
    )