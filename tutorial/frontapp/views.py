from django.shortcuts import render
from django.http import HttpResponse

def getIndexPage(request) :
    return render(
        request,
        "frontapp/index.html",
        {}
    )
    
def htmlview01(request) :
    return render(
        request,
        "frontapp/html/01_html.html",
        {}
    )
    
def linkView(request) :
    return render(
        request,
        "frontapp/html/02_link.html",
        {}
    )
    
def cssView03(request) :
    return render(
        request,
        "frontapp/html/03_css.html",
        {}
    )
    
def cssView04(request) :
    return render(
        request,
        "frontapp/html/04_css.html",
        {}
    )
    
def cssView05(request) :
    return render(
        request,
        "frontapp/html/05_css.html",
        {}
    )
    
def cssView06(request) :
    return render(
        request,
        "frontapp/html/06_css.html",
        {}
    )
    
def tableView07(request) :
    return render(
        request,
        "frontapp/html/07_table.html",
        {}
    )
    
def tableView08(request) :
    
    one_row =  {"mem_id" : "a001",
         "mem_name" : "이순신",
         "mem_area" : "부산 수영구 수영로 777"}
    return render(
        request,
        "frontapp/html/08_table.html",
        one_row,
    )
    
def tableView09(request) :
    
    ### 행렬 리스트 만들기
    # 4행 3열의 행렬데이터
    # 딕셔너리 하나가 행 1개를 의미함
    # 딕셔너리 key가 각 컬럼을 의미합니다.
    mem_list = [{"mem_id" : "a001",
                "mem_name" : "이순신",
                "mem_area" : "부산 수영구 수영로 777"},
                {"mem_id" : "b001",
                "mem_name" : "이순신",
                "mem_area" : "부산 수영구 수영로 777"},
                {"mem_id" : "c001",
                "mem_name" : "이순신",
                "mem_area" : "부산 수영구 수영로 777"},
                {"mem_id" : "d001",
                "mem_name" : "이순신",
                "mem_area" : "부산 수영구 수영로 777"}]
    
    # contexts =  {"mem_id" : "a001",
    #      "mem_name" : "이순신",
    #      "mem_area" : "부산 수영구 수영로 777"}
    
    return render(
        request,
        "frontapp/html/09_table.html",
        {"mem_id" : "a001",
        "mem_name" : "이순신",
        "mem_area" : "부산 수영구 수영로 777",
        "mem_list" : mem_list}
    )
    
def ulView10(request) :
    return render(
        request,
        "frontapp/html/10_ul.html",
        {}
    )
 
def divView11(request) :
    return render(
        request,
        "frontapp/html/11_div.html",
        {}
    )
    
 
def divView12(request) :
    return render(
        request,
        "frontapp/html/12_div.html",
        {}
    )
    
def jsInputFormView(request) :
    return render(
        request,
        "frontapp/html/13_jsInputForm.html",
        {}
    )

# 해당 함수는 사용자로부터 전송받은 데이터를 처리하기 위한 함수
# 처리 이후 어떤 페이지로 보여줄지는 처리 이후 고민
def jsInputCheck(request) :
    ### 사용자가 전송시킨(요청한) 정보를 추출하기
    # - POST 방식으로 전송된 경우
    # - POST라는 딕셔너리 변수에 저장되어 있습니다. 
    if request.method == "POST" :
        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
    
    elif request.method == "GET" :
        mem_id = request.GET["mem_id"]
        mem_pass = request.GET["mem_pass"]
        
    ### DB에 존재하는 아이디/패스워드라고 가정을 한 후
    # - 전송받는 아이디와 패스워드가 아래 변수값과 같은지 비교
    # - 같으면 >>> /front/로 페이지 처리
    # - 다르면 >>> 입력 페이지로 다시 보내기 처리
    id = "boyun"
    pw = "0802"
    
    msg = ""
    if (mem_id == id) & (mem_pass == pw) :
        # msg = "아이디 / 패스워드 일치"
        msg = f"""
                <script type='text/javascript'>
                    alert('아이디[{mem_id}]님이 정상적으로 로그인 되었습니다.');
                    location.href = '/front/';
                </script>
        """
    else :
        # msg = "아이디 / 패스워드 불일치"
        msg = """
                <script type='text/javascript'>
                    alert('아이디 또는 비밀번호 확인 후 다시 로그인하세요.');
                    history.go(-1);
                </script>
        """
    
    ### 함수 호출 잘 되는지 확인을 위한 처리
    return HttpResponse(msg)

def radioView14(request) :
    return render(
        request,
        "frontapp/html/14_radioView.html",
        {}
    )
    
def radio(request) :
    if request.method == "POST" :
        mem_addr = request.POST["mem_addr"]
        mem_addr1 = request.POST["mem_addr1"]
        
    
    
    msg = ""
    if mem_addr == mem_addr1 :
        # msg = "아이디 / 패스워드 일치"
        msg = f"""
                <script type='text/javascript'>
                    location.href = '/front/';
                </script>
        """
    else :
        # msg = "아이디 / 패스워드 불일치"
        msg = f"""
                <script type='text/javascript'>
                    alert('지역이 일치하지 않습니다. 다시 입력하세요.');
                    history.go(-1);
                </script>
        """
    return HttpResponse(msg)
    
def radioView15(request) :
    return render(
        request,
        "frontapp/html/15_radioView.html",
        {
            "mem_addr" : "부산",
            "mem_addr1" : "부산"
        }
    )
    
def radio2(request) :
    if request.method == "POST" :
        mem_addr = request.POST["mem_addr"]
        mem_addr1 = request.POST["mem_addr1"]
        
    msg = ""
    if mem_addr == mem_addr1 :
        # msg = "아이디 / 패스워드 일치"
        msg = f"""
                <script type='text/javascript'>
                    location.href = '/front/';
                </script>
        """
    else :
        # msg = "아이디 / 패스워드 불일치"
        msg = f"""
                <script type='text/javascript'>
                    alert('지역이 일치하지 않습니다. 다시 입력하세요.');
                    history.go(-1);
                </script>
        """
    
    ### 함수 호출 잘 되는지 확인을 위한 처리
    return HttpResponse(msg)

def checkBox16(request) :
    return render(
        request,
        "frontapp/html/16_checkBoxView.html",
        {}
    )
    
def checkBox17(request) :
    ### 지역 텍스트값 받아오기
    mem_addr = request.POST["mem_addr"]
    
    ### 지역 체크박스값 받아오기
    mem_addr1 = request.POST.getlist("mem_addr1")
    
    return render(
        request,
        "frontapp/html/17_checkBox.html",
        {"mem_addr" : mem_addr,
         "mem_addr1" : mem_addr1}
    )
    
def selectBoxView18(request) :
    return render(
        request,
        "frontapp/html/18_selectBoxView.html",
        {}
    )
    
def selectBox19(request) :
    mem_addr_one = request.POST["mem_addr_one"]
    mem_addr_multi = request.POST.getlist("mem_addr_multi")
    return render(
        request,
        "frontapp/html/19_selectBox.html",
        {"mem_addr_one" : mem_addr_one,
         "mem_addr_multi" : mem_addr_multi}
    )