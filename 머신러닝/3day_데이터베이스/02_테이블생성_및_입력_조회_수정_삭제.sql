/*
이 탭은 pknudb영역에서 사용할 구문 에디터 입니다.

<최초 해야할 작업 순서>
- DB 설계를 진행합니다.
- 설계는 보통 상위 레벨의 작업자가 수행합니다.
- DB설계 : 테이블 설계를 수행합니다.
				- 데이블 공간 생성
				- 테이블 공간 내에 사용할 컬럼면, 타입, 사이즈 등 정의		
				- 테이블과 테이블 간의 관계 정의
- DB 설계시 작성되는 문서 : 테이블 정의서, ERD(객체관계도, 테이블관계도), 스크립트(SQL) 명세서
									(이외 다수 있으나, 기본적으로 위해 문서는 있어야함)
									
0. DB : 예를 들어 DB는 엑셀파일 1개로 생각하시면 됩니다.
1. 테이블 생성
- 엑셀 파일 내에 시트를 테이블이라고 생각하시면 됩니다.
- 행열을 관리하는 공간
2. 데이터 입력
3. 데이터 조회, 수정, 삭제 등 SQL구문 처리mysqldb
*/

/*
<테이블 관계>
- 제약조건 : PK 또는 FK와 같은 정의를 제약조건이라고 합니다.
- PK : 고유한 값을 정의하는 컬럼에 정의함
		: PK가 있는 테이블을 "부모 테이블"이라고 칭함
		: 부모테이블 쪽 선 끝에는 바(|)표시가 붙어 있습니다.
- FK : 부모를 참조한다고 해서 "자식 테이블"이라고 칭함
		: 부모 테이블의 PK값과 같은 값이 존재하며, PK를 참조하게 됩니다.		
		: 자식테이블 쪽 선 끝에는 삼바리 또는 닭다리 표시가 붙어 있습니다.
*/

/*
<테이블 컬럼 정의>
- 테이블을 생성할 때는 최초 1개 이상의 컬럼이 존재해야 합니다.
- 컬럼은 영문명으로 작명 합니다.
- 컬럼 하나당 : 차입, 사이즈, 널여부, PK 또는 FK 여부를 정의
- 타입
	- 문자열 : Varchar(가변형. 길이를 알 수 없는 문자)
				  Char(고정형. 코드성 데이터로 길이를 사전에 알고 있는 경우)
	- 숫자 : int
	- 날짜 : datatime
	- 문장 : text(최근에는 많이 사용 안함. Varchar의 사이즈를 늘려서 사용)
- 사이즈(메모리, 자릿수)
	- 영문, 숫자, 특수문자 : 문자 1개 당 1byte 사용됨
	- 한글 : 한글 문자 1개 당 2byte 사용됨
				(사이즈를 지정할 때 한글은 곱하기 2를 해야함)
*/

/*
base.sql 실행
*/

/*
테이블 조회하기
- 회원정보 [조회]하기
- 회원정보는 member 테이블에 있습니다.
- 회원의 모든 정보(모든 컬럼과 같은 의미) 조회하기
*/
SELECT*
FROM member;


-- 회원정보 중에 아이디, 패스워드, 이름만 조회하기
SELECT mem_id, mem_pass, mem_name
FROM member;

-- 회원정보 중에 마일리지의 값이 100이상인 회원아이디와 회원이름 조회하기 
/*
SELECT : 조회할 컬럼명만 정의
FROM : 사용할 테이블명 정의
WHERE : 첫번째 조건 정의
AND : 두번째 조건 정의(없으면 안해도 됨)
*/
SELECT mem_id, mem_name, mem_mileage
FROM member WHERE mem_mileage >= 100;

/*
상품정보 중에 판매가격이 1000원 이상이고, 소비자가격이 2000원 이하인
상품코드, 상품명 조회하기
조건이 두개 이상인 경우 논리 연산자(AND, OR) 사용
*/
SELECT*
FROM prod;

SELECT prod_id, prod_name
FROM prod WHERE prod_sale >= 1000 AND prod_price <= 2000;

/*
회원중에 회원이름이 김은대 또는 이쁜이에 대한 
회원 아이디, 회원 이름 조회하기
*/
SELECT mem_id, mem_name
FROM member WHERE (mem_name = '김은대' or mem_name = '이쁜이');

/*
<정렬하기>
*/
SELECT mem_id, mem_pass, mem_name
-- FROM 절
FROM member 
-- WHERE 절(조건절)
WHERE mem_mileage > 1
-- ORDER BY 절 : SELECT 문장의 가장 마지막에 사용됨
-- 정렬하기 : ORDER BY
-- 오름차순 : ASC, 내림차순 : DESC
-- ORDER BY mem_id ASC; 
-- 컬럼의 위치 순서를 이용해서 정의할 수도 있음
ORDER BY 1 DESC, mem_name ASC;   

/*
<별칭>
- 별칭 : 컬럼명 뒤에 AS 사용
		 : 테이블명 뒤에 별칭(AS는 사용 안함)
		 : 별칭은 가능한 영문으로 AS를 이용해서 사용. 따옴표 없이 사용.
		 
<Select문 실행 순서>
- Database가 컴파일 하는 순서(해석하는 순서)
1번 > 3번 > 4번 > 2번 > 5번
*/

-- 1번
SELECT 
-- 2번
		 mem_id AS id, mem_name AS nm, 
		 mem_id id2, mem_name nm2,
		 mem_id 'id3', mem_name 'nm3',
		 mem_id AS '아이디', mem_name AS '이름'
-- 3번
FROM member 
-- 4번
WHERE mem_mileage > 1 
-- 5번
ORDER BY id DESC, nm ASC;

/* 
회원 중에 76년 1월 1일 이후에 태어난 회원에 대한
아이디, 이름, 주민번호 앞 6자리를 조회해 주세요
정렬은 회원아이디를 기준으로 오름차순
*/

SELECT mem_id AS id, mem_name AS nm, mem_regno1 AS rg
FROM member 
WHERE mem_regno1 > 760101
ORDER BY id ASC;

/* 
상품 판매가격이 15만원 또는 17만원 또는 33만원인 상품을 조회해 주세요
조회 컬럼은 상품명, 판매가격 입니다.
정렬은 판매가격 기준으로 내림차순
*/
SELECT prod_name, prod_sale
FROM prod 
WHERE prod_sale = 150000 OR prod_sale = 170000 OR prod_sale = 330000
ORDER BY prod_sale DESC;

-- or 조건인 경우에는 IN()  함수를 통해서 사용하면 편리
-- 국제 표준 함수로 다른 Database 서버에서도 사용가능한 SQL 구문
SELECT prod_name, prod_sale
FROM prod 
WHERE prod_sale IN (150000, 170000, 330000)
ORDER BY prod_sale DESC;

-- not in : 포함하는 않는
SELECT prod_name, prod_sale
FROM prod 
WHERE prod_sale NOT IN (150000, 170000, 330000)
ORDER BY prod_sale DESC;

/*
- Like : 문자내에 특정 단어 포함여부 확인하기(국제표준)
상품명의 첫글자가 '삼'으로 시작하는 경우만 조회하기
*/
-- 상품명이 '삼'으로 시작하는 경우 찾기
SELECT prod_id, prod_name
FROM prod 
WHERE prod_name LIKE '삼%';

-- 상품명의 두번째 단어가 '성'인 경우 찾기
SELECT prod_id, prod_name
FROM prod 
WHERE prod_name LIKE '_성%';

-- 상품명의 마지막 단어가 '치'인 경우 찾기
SELECT prod_id, prod_name
FROM prod 
WHERE prod_name LIKE '%치';

-- 상품명에 '삼성'이 포함되어 있는 경우 찾기
SELECT prod_id, prod_name
FROM prod 
WHERE prod_name LIKE '%삼성%';

/*
회원의 거주지역이 서울이고, 마일리지 값이 1000이상인 회원에 대한
아이디, 이름, 주소(앞), 주소(뒤), 마일리지 조회하기
*/
SELECT mem_id, mem_name, mem_add1, mem_add2, mem_mileage
FROM member 
WHERE mem_add1 LIKE '서울%' AND mem_mileage >= 1000;

-- 컬럼간에 합치기
SELECT mem_id, mem_name, mem_mileage, concat(mem_add1,' ', mem_add2)
FROM member 
WHERE mem_add1 LIKE '서울%' AND mem_mileage >= 1000;

/*
회원 생일이 1975년도에 태어난 회원만 조회해 주세요
*/
SELECT*
FROM member 
WHERE mem_bir LIKE '1975%';

/*
회원 생일이 1975년 1월 1일부터 1975년 10월 31일 사이에 태어난 회원만 조회해 주세요
*/
-- 날짜 타입의 컬럼을 이요해서 조건처리하는 경우에는
-- : 날짜 포멧을 적용하면 됩니다. (크기비교, 문자비교 모두 가능)
-- : 날짜 포멧 -> 00000000, 0000-00-00, 0000/00/00, 0000.00.00
SELECT*
FROM member 
WHERE mem_bir LIKE '1975%' AND mem_bir not LIKE '%-11-%' AND mem_bir not LIKE '%-12-%';

SELECT*
FROM member 
WHERE mem_bir >= '1975-01-01' AND mem_bir <= '1975-10-31';

-- 범위 조건 : Between A And B
SELECT*
FROM member 
WHERE mem_bir BETWEEN '1975-01-01' AND '1975-10-31';

/*
대표적 문자열 함수 : Substring(컬럼면, 시작위치, 끝위치)
- 조회할 컬럼명에 사용가능 또는 조건절 컬럼명에도 사용가능
*/
-- 회원의 거주 지역만 추출하기
-- 회원 전체 조회
SELECT mem_name, mem_add1, SUBSTRING(mem_add1, 1, 2) AS mem_area
FROM member;

SELECT mem_name, mem_add1, SUBSTRING(mem_add1, 1, 2) AS mem_area
FROM member
WHERE SUBSTRING(mem_add1, 1, 2) = '서울';

/*
회원의 성씨가 김씨이고, 지역이 서울 또는 대전이며,
기념일에 결혼이라는 단어가 포함된 회원에 대한 정보조회
조회 컬럼은 회원이름, 지역, 기념일명
*/
SELECT mem_name, mem_memorial, SUBSTRING(mem_add1, 1, 2)
FROM member
WHERE mem_memorial LIKE '결혼%' 
AND mem_name LIKE '김%' 
AND SUBSTRING(mem_add1, 1, 2) IN ('서울', '대전');

SELECT mem_name, SUBSTRING(mem_memorial, 1, 2), SUBSTRING(mem_add1, 1, 2)
FROM member
WHERE mem_name LIKE '김%' 
AND SUBSTRING(mem_memorial, 1, 2) = '결혼'
AND SUBSTRING(mem_add1, 1, 2) IN ('서울', '대전');

/*
회원의 아이디가 a001인 회원이 가지고 있는 마일리지보다 큰 회원 조회하기
조회 컬럼은 회원 아이디, 회원 마일리지

- 서브쿼리(SubQuery)
	- Select문 안에 Selct문을 사용하는 경우에 이를 서브커리라고 칭합니다.
*/
SELECT mem_id, mem_mileage
FROM member
WHERE mem_mileage >= (SELECT mem_mileage FROM member WHERE mem_id = 'a001');

/*
장바구니 테이블에는 회원들이 주문한 경우에 정보가 담깁니다.
한번도 주문한 적이 없는 회원의 아이디와 회원이름을 조회해 주세요.
*/
SELECT *
FROM cart;

SELECT mem_id, mem_name
FROM member
WHERE mem_id NOT IN (SELECT cart_member FROM cart);
