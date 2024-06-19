from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
### models.py DB정보 가지고 오기
from .models import Member, Cart

### mysql 루트 함수 만들기
# http://127.0.0.1:8000/mysql/ 요청 처리
def index(request) :
    return render(
        request,
        "mysqlapp/index.html",
        {}
    )
    
### /mysql/mem_list/
def getMemberList(request) :
    
    ### 회원 전체 정보 가지고 오기
    # - 전체 행(objects)과 열(all)의 정보를 가지고 옵니다.
    #   (Member 클래스에 정의된 변수(컬럼)이 전체입니다.)
    # - Member.objects.all()은 -> 아래 SQL구문과 같음 
    #   : Select mem_id, mem_pass, mem_name, mem_add1 From member
    # - 조회 결과 형태는 아래와 같음
    #   [{'a001', 'asdf', '홍길동', '부산...'}, {...}, {...}, ....]
    # - models.py를 사용하는 방식을 Django의 ORM 방식이라고 합니다
    # - ORM : 객체(class) 기반의 매핑방식으로 Django 프레임워크에 의해 관리됩니다.
    #       : SQL 구문 없이 객체 기반으로 사용되는 방식(융통성이 조금 떨어집니다.)
    mem_list = Member.objects.all()
    
    return render(
        request,
        "mysqlapp/member/mem_list.html",
        {"mem_list" : mem_list}
    )

### /mysql/mem_view/
def getMemberView(request) :
    
    ### mem_list에서 전송된 mem_id의 값 받기
    # - key가 없으면 오류 발생
    mem_id = request.GET["mem_id"]
    # - key가 없으면 ""으로 리턴됨(오류 발생 안함)
    #   : 주로 딕셔너리에서 값 조회시 사용되는 방식
    mem_id = request.GET.get("mem_id")
    
    ### 해당 mem_id에 대한 정보 조회하기 : 1건 조회
    # - get(Member.mem_id = 전송받은 mem_id값)
    # - SQL 구문 : Select mem_id, mem_pass, mem_name, mem_add1 From member Where mem_id = '전송받은값'
    # - 결과 형태 : {'', '', '', ''}
    mem_view = Member.objects.get(mem_id = mem_id)
    
    return render(
        request,
        "mysqlapp/member/mem_view.html",
        {"mem_id" : mem_id,
         "mem_view" : mem_view}
    )

### /mysql/mem_update_view/
def getMemberUpdateView(request) :
    mem_id = request.GET.get("mem_id")
    
    mem_view = Member.objects.get(mem_id = mem_id)
    
    return render(
        request,
        "mysqlapp/member/mem_update_view.html",
        {"mem_id" : mem_id,
         "mem_view" : mem_view}
    )
    
### /mysql/mem_update/
def getMemberUpdate(request) :
    mem_id   = request.POST.get("mem_id")
    mem_pass = request.POST.get("mem_pass")
    mem_add1 = request.POST.get("mem_add1")
    
    # msg = f"아이디 = {mem_id} / 패스워드 = {mem_pass} / 주소1 = {mem_add1}"
    ### 데이터베이스에 수정 요청하기
    # - filter() : SQL 구문의 where 절과 동일
    # - update() : 수정할 값 정의
    # - SQL 구문 
    #   Update member 
    #     Set mem_pass = 수정할값,
    #         mem_add1 = 수정할값
    #   Where mem_id = 아이디값
    result_cnt = Member.objects.filter(mem_id=mem_id).update(mem_pass=mem_pass, 
                                                               mem_add1=mem_add1)
    
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
                alert('수정에 실패하였습니다. 수정 정보를 다시 확인하여 주세요!!');
                history.go(-1);
            </script>
        """
    return HttpResponse(msg)


############[주문내역/장바구니 영역]#############

### /mysql/cart_list/
def getCartList(request) :
    ### 정렬 : order_by()
    #        : 마이너스(-) 표시 : 내림차순, 안넣으면 오름차순
    cart_list = Cart.objects.all().order_by("-cart_no", "cart_member")
    
    return render(
        request,
        "mysqlapp/cart/cart_list.html",
        {"cart_list" : cart_list}
    )
    
### /mysql/cart_view/
def getCartView(request) :
    
    cart_no   = request.GET.get("cart_no")
    cart_prod = request.GET.get("cart_prod")
    
    cart_view = Cart.objects.get(cart_no=cart_no, cart_prod=cart_prod)
    
    return render(
        request,
        "mysqlapp/cart/cart_view.html",
        {"cart_no" : cart_no,
         "cart_prod" : cart_prod,
         "cart_view" : cart_view}
    )
    
### /mysql/cart_update_view/
def getCartUpdateView(request) :
    
    cart_no   = request.GET.get("cart_no")
    cart_prod = request.GET.get("cart_prod")
    
    cart_view = Cart.objects.get(cart_no=cart_no, cart_prod=cart_prod)
    
    return render(
        request,
        "mysqlapp/cart/cart_update_view.html",
        {"cart_no" : cart_no,
         "cart_prod" : cart_prod,
         "cart_view" : cart_view}
    )
    
### /mysql/cart_update/
def getCartUpdate(request) :
    cart_no   = request.POST.get("cart_no")
    cart_prod = request.POST.get("cart_prod")
    cart_qty  = request.POST.get("cart_qty")
    
    result_cnt = Cart.objects.filter(cart_no=cart_no,
                                     cart_prod=cart_prod).update(cart_qty=cart_qty)
    
    ### 수정 성공한 경우
    if result_cnt > 0 :
        msg = f"""
            <script type='text/javascript'>
                alert('성공적으로 수정되었습니다.');
                location.href = '/mysql/cart_view/?cart_no={cart_no}&cart_prod={cart_prod}';
            </script>
        """
    else :
        ### 수정 실패
        msg = """
            <script type='text/javascript'>
                alert('수정에 실패하였습니다. 수정 정보를 다시 확인하여 주세요!!');
                history.go(-1);
            </script>
        """
    return HttpResponse(msg)


### /mysql/cart_delete/
def getCartDelete(request) :
    
    cart_no   = request.GET.get("cart_no")
    cart_prod = request.GET.get("cart_prod")
    
    ### DB에 삭제 요청하기
    # - SQL 구문 : Delete From cart Where cart_no=전달받은값 and cart_prod=전달받은값
    rs_cnt, _ = Cart.objects.filter(cart_no=cart_no, cart_prod=cart_prod).delete()
    
    ## msg = f"rs_cnt={rs_cnt}"
    ### rs_cnt가 0보다 크면 삭제 성공, 0이면 삭제 실패...처리하기
    ### 삭제 성공한 경우
    if rs_cnt > 0 :
        msg = f"""
            <script type='text/javascript'>
                alert('성공적으로 삭제되었습니다.');
                location.href = '/mysql/cart_list/';
            </script>
        """
    else :
        ### 삭제 실패
        msg = """
            <script type='text/javascript'>
                alert('삭제에 실패하였습니다.');
                history.go(-1);
            </script>
        """
    
    return HttpResponse(msg)

### /mysql/cart_insert_view/
def getCartInsertView(request) :
    return render(
        request,
        "mysqlapp/cart/cart_insert_view.html",
        {}
    )
## 2024041300001 P101000002    
### /mysql/cart_insert/
def getCartInsert(request) :
    try :
        cart_no     = request.POST.get("cart_no")
        cart_member = request.POST.get("cart_member")
        cart_prod   = request.POST.get("cart_prod")
        cart_qty    = request.POST.get("cart_qty")
        
        Cart.objects.create(cart_no=cart_no, cart_member=cart_member,
                                        cart_prod=cart_prod, cart_qty=cart_qty)
    except :
        ### 입력 실패
        msg = """
            <script type='text/javascript'>
                alert('입력에 실패하였습니다. 입력 값을 확인하여 주세요!!');
                history.go(-1);
            </script>
        """
        return HttpResponse(msg)
    
    msg = f"""
        <script type='text/javascript'>
            alert('성공적으로 입력 되었습니다.');
            location.href = '/mysql/cart_list/';
        </script>
    """
    return HttpResponse(msg)


############[페이징 처리]#############
# - 페이징 처리를 위해서 필요한 라이브러리 설치
# - Django에서 지원하는 페이징 처리 라이브러리 : Paginator
# - 라이브러리 설치 : pip install Paginator

from django.core.paginator import Paginator

### /mysql/cart_list_page/
def getCartListPaging(request) :
    
    ####### [페이징 처리 영역] ######
    # - 페이지 번호로 사용할 변수 정의
    # - cart_list.html 페이지와 주고 받을 페이지 번호
    #   (사용자가 선택한 페이지 번호를 유지하기 위하여, 
    #    페이지 정보를 주고 받아야 합니다.)
    # - get("전송받은 name명", "전송받은 값이 없을 때 사용할 기본값")
    #   --> 최초에 cart_list.html 페이지가 실행 될 때는 page 값은 전송되어 오지 않습니다.    
    now_page = request.GET.get("page", "1")
    # - 웹 브라우저를 통해 전송받는 모든 데이터의 타입은 문자열 입니다.
    # - 숫자값을 사용하려면 형변환 시킵니다.
    now_page = int(now_page)
    ################################
    
    ### 정렬 : order_by()
    #        : 마이너스(-) 표시 : 내림차순, 안넣으면 오름차순
    cart_list = Cart.objects.all().order_by("-cart_no", "cart_member")
    
    ####### [페이징 처리 영역] ######
    # - 한 페이지에 보여줄 행의 갯수 정의 : 보통 10개씩..또는 자유롭게..
    num_row = 10
    
    ### DB로부터 조회한 데이터를 Paginator 라이브러리에 넣어줍니다.
    # - 한 페이지 보여질 행의 갯수도 함께 넣어 줍니다.
    # - 라이브러리 역할 : 한 페이지에 보여줄 행의 갯수를 기준으로 전체 행을 분리하는 작업
    # - 10개씩 분리하여 각각을 페이지 번호로 관리하고 있습니다.
    p = Paginator(cart_list, num_row)
    
    ### 현재 페이지 번호에 해당하는 10건의 데이터 추출
    # - table 태그의 행의 갯수에 사용할 데이터
    rows_data = p.get_page(now_page)
    
    ### 하단의 페이지 번호 표시 부분
    # - 시작 페이지 번호 계산하기 (화면에 보이는 페이지번호의 시작번호를 1, 11, 21 처럼 시작되게 처리)
    start_page = (now_page - 1) // num_row * num_row + 1
    
    # - 종료 페이지 번호 계산하기 (화면에 보이는 페이지번호의 끝번호는 10, 20, 30 처럼 끝나게 처리)
    end_page = start_page + (num_row - 1)
    
    ### 종료 페이지 번호(end_page)가 전체 페이지 번호(p.num_pages)보다 크면
    # - 종표 페이지 번호를 전체 페이지 번호로 처리
    if end_page > p.num_pages :
        end_page = p.num_pages
        
    ### 이전 및 다음 버튼 보여줄지 말지 여부 처리를 위한 변수 정의
    is_prev = False
    is_next = False
    
    ### 시작페이지 번호(start_page)가 1보다 크면 이전(is_prev)버튼 보이기
    if start_page > 1 :
        is_prev = True
        
    ### 종료페이지 번호(end_page)가 전체 페이지 번호(p.num_pages)보다 작으면
    #   다음(is_next) 버튼 보이기
    if end_page < p.num_pages :
        is_next = True
    ################################
        
    return render(
        request,
        "mysqlapp/cart_page/cart_list.html",
        {
            ### 실제 보여줄 10개씩의 행 데이터
            "cart_list"  : rows_data,
            ### 현재 페이지 번호
            "now_page"   : now_page,
            ### 한 페이지에 시작부터 끝까지 보여줄 번호
            "page_range" : range(start_page, end_page + 1),
            ### 이전버튼 보여줄지 여부
            "is_prev"    : is_prev,
            ### 다음버튼 보여줄지 여부
            "is_next"    : is_next,
            ### 시작페이지 번호
            "start_page" : start_page
        }
    )
    
    
########## [세션(session) 처리 > 로그인 유지] #######
# - 세션처리 설정 : settings.py에 아래 추가
# - 브라우저가 닫히면 사용자 로그인 정보 삭제하기
#  SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# - django에서 제공하는 session 정보를 이용하기 위해서는
#  --> python manage.py makemigrations 실행(app 이름 없이 실행)
#  --> python manage.py migrate 실행
# - session 유지 정보는 request 객체에서 관리합니다.

### /mysql/login_logout_view/
def login_logout_view(request) :
    return render(
        request,
        "mysqlapp/login/login_logout_view.html",
        {}
    )
    
### /mysql/login/
from django.db.models import Count

def login(request) :
    mem_id   = request.POST.get("mem_id")
    mem_pass = request.POST.get("mem_pass")
    
    ### 전송받은 아이디와 패스워드가 데이터베이스 정보에 존재하는 사용자인지 확인
    # - 존재한다면 세션(session)에 담아서 로그인 유지 시키기
    # - 존재하지 않는다면 이전페이지로 이동시켜서 아이디/패스워드 확인 후 입력하라고 메시지 처리
    # - 세션(session)은 딕셔너리 타입으로 정의된 변수입니다.
    # - SQL 구문 : Select count(mem_id) from member where mem_id=mem_id and mem_pass=mem_pass
    rs_dict = Member.objects.filter(mem_id=mem_id, mem_pass=mem_pass).aggregate(Count("mem_id"))
    
    ### 데이터가 있는지 없는지 확인
    # - 아이디와 패스워드 정보가 없다면....
    if rs_dict['mem_id__count'] == 0 :
        msg = """
            <script type='text/javascript'>
                alert('아이디 또는 패스워드가 일치하지 않습니다. 다시 확인 후 로그인 해주세요!!');
                history.go(-1);
            </script>
        """
        return HttpResponse(msg)
    
    ### 아이디와 패스워드 정보가 있다면...세션에 담기
    request.session["ses_mem_id"] = mem_id
        
    ## msg = f"mem_id = {mem_id} / mem_pass = {mem_pass} / rs_dict = {rs_dict['mem_id__count']}"
    ## return HttpResponse(msg)
    return render(
        request,
        "mysqlapp/login/login_logout_view.html",
        {}
    )
    
### 로그아웃 처리 : /mysql/logout/
def logout(request) :
    ### 로그아웃 처리는 -> 세션의 정보를 삭제하면 됩니다.
    # - 딕셔너리 정보 삭제하기
    request.session.flush()
    
    msg = f"""
        <script type='text/javascript'>
            alert('로그아웃 되었습니다.');
            location.href = '/mysql/login_logout_view/';
        </script>
    """
    return HttpResponse(msg)