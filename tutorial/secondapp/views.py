from django.shortcuts import render
from django.http import HttpResponse

def getIndexPage(request) :
    return render(
        request,
        "secondapp/index.html",
        {}
    )
    
def LoginPage(request) :
    return render(
        request,
        "secondapp/login.html",
        {}
    )
    
def LoginCheck(request) :
    if request.method == "POST" :
        mem_name = request.POST["mem_name"]
        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
        
    id = "boyun"
    pw = "0802"
    
    msg = ""
    if (mem_id == id) & (mem_pass == pw) :
        msg = f"""
                <script type='text/javascript'>
                    alert('[{mem_name}]님 로그인 되었습니다.');
                    location.href = '/second/';
                </script>
        """
    else :
        msg = """
                <script type='text/javascript'>
                    alert('일치하는 정보가 없습니다.');
                    history.go(-1);
                </script>
        """
    
    ### 함수 호출 잘 되는지 확인을 위한 처리
    return HttpResponse(msg)
