from django.shortcuts import render

# Create your views here.
def ExcelPage(request) :
    return render(
        request,
        "excelapp/excel.html",
        {}
    )
    
    