from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

### http://127.0.0.1:8000/front/
def index(request) :
    return render(
        request,
        "frontapp/index.html",
        {}
    )
    
### http://127.0.0.1:8000/front/01_html/
def htmlView01(request) :
    return render(
        request,
        "frontapp/html/01_html.html",
        {}
    )
    
### http://127.0.0.1:8000/front/02_link/
def linkView(request) :
    return render(
        request,
        "frontapp/html/02_link.html",
        {}
    )
    
### http://127.0.0.1:8000/front/03_css/
def cssView03(request) :
    return render(
        request,
        "frontapp/html/03_css.html",
        {}
    )
    
### http://127.0.0.1:8000/front/04_css/
def cssView04(request) :
    return render(
        request,
        "frontapp/html/04_css.html",
        {}
    )
    
### http://127.0.0.1:8000/front/05_css/
def cssView05(request) :
    return render(
        request,
        "frontapp/html/05_css.html",
        {}
    )
    
### http://127.0.0.1:8000/front/06_css/
def cssView06(request) :
    return render(
        request,
        "frontapp/html/06_css.html",
        {}
    )
    
### http://127.0.0.1:8000/front/07_table/
def tableView07(request) :
    return render(
        request,
        "frontapp/html/07_table.html",
        {}
    )
    
### http://127.0.0.1:8000/front/08_table/
def tableView08(request) :    
    
    one_row = {"mem_id" : "a001",
                "mem_name" : "이순신",
                "mem_area" : "부산 수영구 수영로 777"}
    
    return render(
        request,
        "frontapp/html/08_table.html",
        one_row
    )
    
### http://127.0.0.1:8000/front/09_table/
def tableView09(request) :    
    
    ### 행렬 리스트 만들기
    ### 4행 3열의 행렬 데이터
    # - 딕셔너리 하나가 행 1개를 의미함
    #   -- 딕셔너리 key가 각 컬럼을 의미합니다.
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
    
    # contexts = {"mem_id" : "a001",
    #             "mem_name" : "이순신",
    #             "mem_area" : "부산 수영구 수영로 777"}
    
    return render(
        request,
        "frontapp/html/09_table.html",
        {"mem_id" : "a001",
         "mem_name" : "이순신",
         "mem_area" : "부산 수영구 수영로 777",
         "mem_list" : mem_list}
    )
    
### http://127.0.0.1:8000/front/10_ul/
def ulView10(request) :    
    
    return render(
        request,
        "frontapp/html/10_ul.html",
        {}
    )
    
    
### http://127.0.0.1:8000/front/11_div/
def divView11(request) :    
    
    return render(
        request,
        "frontapp/html/11_div.html",
        {}
    )
    
### http://127.0.0.1:8000/front/12_div/
def divView12(request) :    
    
    return render(
        request,
        "frontapp/html/12_div.html",
        {}
    )

### http://127.0.0.1:8000/front/13_jsInputForm/
def jsInputFormView(request) :    
    
    return render(
        request,
        "frontapp/html/13_jsInputForm.html",
        {}
    )

### http://127.0.0.1:8000/front/14_jsInputCheck/
# - 해당 함수는 사용자로부터 전송받은 데이터를 처리하기 위함 함수
# - 처리 이후 어떤 페이지로 보여줄지는 처리 이후 고민....
def jsInputCheck(request) : 
    ### 사용자가 전송시킨(요청한) 정보를 추출하기
    # - POST 방식으로 전송된 경우
    # - POST라는 딕셔너리 변수에 저장되어 있습니다.
    if request.method == "POST" : 
        mem_id   = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
        
    elif request.method == "GET" :
        mem_id   = request.GET["mem_id"]
        mem_pass = request.GET["mem_pass"]
    
    ### DB에 존재하는 아이디/패스워드라고 가정을 한 후 
    # - 전송받은 아이디와 패스워드가 아래 변수값과 같은지 비교
    # - 같으면 >>> /front/로 페이지 처리
    # - 다르면 >>> 입력 페이지로 다시 보내기 처리
    id = "a001"
    pw = "asdf"
    
    msg = ""
    if (id == mem_id) & (pw == mem_pass):
        # msg = "아이디 / 패스워드 일치"
        msg = f"""
              <script type='text/javascript'>
                alert('아이디[{mem_id}]님 정상적으로 로그인 되었습니다.');
                location.href = '/front/';
              </script>
        """
    else :
        # msg = "아이디 또는 패스워드가 일치하지 않습니다."
        msg = """
              <script type='text/javascript'>
                alert('아이디 또는 패스워드 확인 후 다시 로그인해 주시기 바랍니다.');
                history.go(-1);
              </script>
        """
    
       
    ### 함수 호출 잘 되는지 확인을 위해 임시로 아래 처리
    return HttpResponse(msg)


### http://127.0.0.1:8000/front/14_radioView/
def radioView14(request) :    
    
    return render(
        request,
        "frontapp/html/14_radioView.html",
        {}
    )
    
### http://127.0.0.1:8000/front/15_radio/
def radio(request) :        
    ### 요청받은 정보 추출하기
    mem_addr  = request.POST["mem_addr"]
    mem_addr1 = request.POST["mem_addr1"]
    
    ### 부산인지 아닌지 확인하기
    msg = ""
    if mem_addr == mem_addr1 :
        msg = f"""
            <script type='text/javascript'>
                alert('{mem_addr} 지역을 입력하셨네요!!');
                location.href = '/front/';
            </script>
        """
        
    else :
        msg = f"""
            <script type='text/javascript'>
                alert('지역이 일치하지 않습니다. 다시 입력하여 주세요!!');
                history.go(-1);
            </script>
        """
    
    return HttpResponse(msg)


### http://127.0.0.1:8000/front/15_radioView/
def radioView15(request) :    
    
    return render(
        request,
        "frontapp/html/15_radioView.html",
        {"mem_addr" : "부산",
         "mem_addr1" : "부산"}
    )
### http://127.0.0.1:8000/front/16_radio/
def radio2(request) :        
    ### 요청받은 정보 추출하기
    mem_addr  = request.POST["mem_addr"]
    mem_addr1 = request.POST["mem_addr1"]
    
    ### 부산인지 아닌지 확인하기
    msg = ""
    if mem_addr == mem_addr1 :
        msg = f"""
            <script type='text/javascript'>
                alert('{mem_addr} 지역을 입력하셨네요!!');
                location.href = '/front/';
            </script>
        """
        
    else :
        msg = f"""
            <script type='text/javascript'>
                alert('지역이 일치하지 않습니다. 다시 입력하여 주세요!!');
                history.go(-1);
            </script>
        """
    
    return HttpResponse(msg)


### http://127.0.0.1:8000/front/16_checkBoxView/
def checkBoxView16(request) :    
    
    return render(
        request,
        "frontapp/html/16_checkBoxView.html",
        {}
    )

### http://127.0.0.1:8000/front/17_checkBox/
def checkBox17(request) :    
    ### 지역 텍스트값 받아오기
    mem_addr = request.POST["mem_addr"]
    
    ### 지역 체크박스값 받아오기
    ## mem_addr1 = request.POST["mem_addr1"]
    mem_addr1 = request.POST.getlist("mem_addr1")
    
    return render(
        request,
        "frontapp/html/17_checkBox.html",
        {"mem_addr" : mem_addr,
         "mem_addr1" : mem_addr1}
    )

### http://127.0.0.1:8000/front/18_selectBoxView/
def selectBoxView18(request) : 
    return render(
        request,
        "frontapp/html/18_selectBoxView.html",
        {}
    )
    
### http://127.0.0.1:8000/front/19_selectBox/
def selectBox19(request) : 
    mem_addr_one = request.POST["mem_addr_one"]
    
    mem_addr_multi = request.POST.getlist("mem_addr_multi")
    
    return render(
        request,
        "frontapp/html/19_selectBox.html",
        {"mem_addr_one" : mem_addr_one,
         "mem_addr_multi" : mem_addr_multi}
    )
    
    
############## [레이아웃 분리 : include] #############
### http://127.0.0.1:8000/front/20_include/
def includeView(request) :
    return render(
        request,
        "frontapp/include/20_include_view.html",
        {}
    )
    
    
############## [레이아웃 분리 : extend] #############
### http://127.0.0.1:8000/front/21_extend_layout/
def extendLayoutView(request) :
    return render(
        request,
        "frontapp/extend/21_extend_layout.html",
        {}
    )
    
### http://127.0.0.1:8000/front/22_section/
def extendSection(request) :
    return render(
        request,
        "frontapp/extend/22_section.html",
        {}
    )
    
### http://127.0.0.1:8000/front/23_table/
def extendTable(request) :
    return render(
        request,
        "frontapp/extend/23_table.html",
        {}
    )
    
### http://127.0.0.1:8000/front/01_bootstrap/
def bootstrap01(request) :    
    
    return render(
        request,
        "frontapp/bootstrap/01_bootstrap.html",
        {}
    )
    
### http://127.0.0.1:8000/front/02_bootstrap_table/
def bootstrap_table02(request) :    
    
    return render(
        request,
        "frontapp/bootstrap/02_bootstrap_table.html",
        {}
    )
    
### Anscombe 시각화 이미지 만들기
### data_view.py의 Data_View 클래스 import 하기
from frontapp.data_view.data_view import Data_View

### /front/data_view/
def createAnscombe_Image(request) :
    ### 클래스 생성하기
    data_view = Data_View()
    
    return render(
        request,
        "frontapp/data_view/data_view.html",
        {}
    )
    
### 모델을 이용하여 예측결과 확인하기
### ml_predict.py의 ML_Predict 클래스 import 하기
from frontapp.ml_predict.ml_predict import ML_Predict

### /front/ml_predict/
def getML_Predict(request) :
    ### 실제 예측하고자 하는 값은 html form을 통해 입력받은 수 
    # request.GET[] or POST[]로 받아서 아래 리스트에 넣어주면 됩니다.
    random_X = [[ 9.9 ,  2.2 ,  3.27]]
    
    ### 클래스 생성하기
    ml_pred = ML_Predict()
    
    ### random_X값을 이용하여 예측해보기(예측함수 호출)
    pred_y = ml_pred.getModelPredict(random_X)
    
    return HttpResponse(f'예측값 : {pred_y}')