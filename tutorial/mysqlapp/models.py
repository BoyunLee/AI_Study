from django.db import models
### 컬럼의 문자열 타입과 매핑됨
from django.db.models.fields import CharField
### 컬럼의 숫자형 타입과 매핑됨
from django.db.models.fields import IntegerField

# Create your models here.

### 아래 테이블 클래스가 만들어지면 항상 아래 명령을 프롬프트에서 수행해여합니다.
# 클래스 생성이 아닌경우에는 아래 수행은 하지 않아도 됩니다.
# (클래스 내부에 컬럼변수 추가 또는 속성 수정인 경우는 안해도 되지만,
#  혹여나 수정 후 데이터 조회/수정/삭제/입력이 잘 안되는 경우에는 아래 명령어 수행)
# > python manage.py makemigrations mysqlapp(models.py 파일이 있는 app 이름)
# > python manage.py migrate

### 데이터베이스와 관련하여 사용할 테이블을 형상화 시키기
# 형상은 클래스로 생성합니다.
# 클래스 이름 및 사용하는 변수명은 
# 모두 실제 DB의 사용할 테이블명과 컬럼명과 동일해야 합니다.

### 회원정보 데이블 매핑하기 위한 클래스 생성하기
class Member(models.Model) :
    mem_id = CharField(primary_key=True, max_length=15, null=False)
    mem_pass =  CharField(max_length=15, null=False)
    mem_name =  CharField(max_length=10, null=False)
    mem_add1 =  CharField(max_length=60, null=False)
    
    ### 내부 클래스 정의하기 : 메타클래스(django model 생성 문법)
    # 아래는 규칙적으로 사용
    class Meta : 
        ### 실제 DB의 테이블 이름 정의
        db_table = 'member'
        
        ### 사용할 app 이름 정의
        app_label = 'mysqlapp'
        
        ### 외부 DB에 테이블이 존재하는지 여부
        # 존재하면 = False, 존재하지 않으면 = True
        # 일반적으로 Database는 사전에 설계되어 테이블이 생성되어 있기에
        # 대부분 False를 사용하면 됩니다.
        managed = False