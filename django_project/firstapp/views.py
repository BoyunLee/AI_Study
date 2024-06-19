from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

### index/ 페이지주소로 들어오는 경우 호출되는 함수
# 사용자의 요청 정보는 request 객체(요청객제)에 담겨 있습니다.
def getIndexPage(request) :
    ### 응답할 내용 : html 문법에 따라 작성함
    # msg = """
    #     <b>
    #        firstapp 내에 views.py의 getIndexPage가 호출되었습니다.
    #     </b>
    # """
    # firstapp 내에 views.py의 getIndexPage가 호출되었습니다.
    ### 응답객체(response 객체라고 합니다.)
    # 요청한 사용자의 PC IP주소로 응답해줍니다.
    # return HttpResponse(msg)
    
    return render(
        request,
        "firstapp/index.html",
        {}
    )


### http://127.0.0.1:8000/index3/ 처리
def getIndex3(request) :
    msg = "이곳은 index3 페이지 입니다."
    return HttpResponse(msg)

