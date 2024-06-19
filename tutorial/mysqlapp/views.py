from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
### model.py DB정보 가지고 오기
from .models import Member

### mysql 루트 함수 만들기
### http://127.0.0.1:8000/mysql/ 요청 처리
def index(request) :
    return render(
        request,
        "mysqlapp/index.html",
        {}
    )
    
### http://127.0.0.1:8000/mysql/mem_list/ 요청 처리
def getMenberList(request) :
    
    ### 회원 전체 정보 가지고 오기
    # 전체 행(object)과 열(all)의 정보를 가지고 옵니다.
    # (Member 클래스에 정의된 변수(컬럼)이 전체입니다.)
    # Member.objests.all()은 -> 아래 구문과 같음
    # : Select mem_id, mem_pass, mem_name, mem_add1 From memder
    # 조회 결과 형태는 아래와 같음
    # [{'a001', 'asdf', '홍길동', '부산'}, {...}, {...}, ...]
    # model.py를 사용하는 방식을 Django의 ORM방식이라고 합니다
    # ORM : 객체(class) 기반의 매핑방식으로 Django 프레임워크에 의해 관리됩니다.
    #     : SQL 구문 없이 객체 기반으로 사용되는 방식(융통성이 조금 떨어집니다.)
    mem_list = Member.objects.all() 
        
    return render(
        request,
        "mysqlapp/member/mem_list.html",
        {"mem_list" : mem_list}
    )

### http://127.0.0.1:8000/mysql/mem_view/ 요청 처리
def getMenberView(request) :
    ### mem_list에서 전송된 mem_id의 값 받기
    # key가 없으면 오류 발생
    mem_id = request.GET["mem_id"]
    # key가 없으면 ""으로 리턴됨(오류 발생 안함)
    # 주로 딕셔너리에서 값 조회시 사용되는 방식
    mem_id = request.GET.get("mem_id")
    
    ### 해당 mem_id에 대한 정보 조회하기 : 1건 조회
    # get(Member.mem_id = 전송받은 mem_id 값)
    # SQL 구문 = Select mem_id, mem_pass, mem_name, mem_add1 From member Where mem_id = '전송 받은 값'
    # 결과 형태 : {'', '', '', ''}
    mem_view = Member.objects.get(mem_id = mem_id)
    
    return render(
        request,
        "mysqlapp/member/mem_view.html",
        {"mem_id" : mem_id, 
         "mem_view" : mem_view}
    )

### http://127.0.0.1:8000/mem_update_view/ 요청 처리
def getMenberUpdateView(request) :
    mem_id = request.GET.get("mem_id")
    mem_view = Member.objects.get(mem_id = mem_id)
    
    return render(
        request,
        "mysqlapp/member/mem_update_view.html",
        {"mem_id" : mem_id,
         "mem_view" : mem_view}
    )
    
### http://127.0.0.1:8000/mem_update/ 요청 처리
def getMenberUpdate(request) :
    mem_id = request.POST.get("mem_id")
    mem_pass = request.POST.get("mem_pass")
    mem_add1 = request.POST.get("mem_add1")
    
    # msg = f"아이디 = {mem_id} / 패스워드 = {mem_pass} / 주소1 = {mem_add1}"
    ### 데이터베이스에 수정 요청하기
    # filter() : SQL 구문의 where 절과 동일
    # update() : 수정할 값 정의
    # SQL 구문
    # Update member
    # Set mem_pass = 수정할 값,
    #     mem_add1 = 수정할 값
    # Where mem_id = 아이디값
    result_cnt = Member.objects.filter(mem_id=mem_id).update(mem_pass = mem_pass, mem_add1 = mem_add1)
    
    ### 수정 성공한 경우
    if result_cnt > 0 :
        msg = f"""
            <script type='text/javascript'>
                alert('성공적으로 수정되었습니다.');
                location.href = '/mysql/mem_view/?mem_id={mem_id}';
            </script>
        """
    else :
    ### 수정 실패
        msg = """
            <script type='text/javascript'>
                alert('수정에 실패하였습니다.');
                history.go(-1);
            </script>
        """
    
    return HttpResponse(msg)