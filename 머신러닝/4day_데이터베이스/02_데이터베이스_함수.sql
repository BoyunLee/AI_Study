/*
<함수>
- 데이터베이스 시스템별로 함수 이름은 모두 상이하며 개념은 모두 동일
- 함수이름도 유사하게 존재함
- 국제표준을 따르지 않으며, DB 사용자에게 편의성을 제공하기 위해서
  Database를 제공하는 기업에서 만들어 놓은 기능
*/

/*
Replace(컬럼명, 찾을값, 바꿀값) : 값 치환하기
*/
SELECT prod_name, REPLACE(prod_name, '모니터', '넌누구?') AS NAME
FROM prod;

/*
회원의 성씨가 이씨인 회원들에 대해서
성을 리씨로 바꿔서 조회
*/
SELECT mem_name, CONCAT(REPLACE(SUBSTRING(mem_name, 1, 1), '이', '리'), SUBSTRING(mem_name, 2, 2)) AS NAME 
FROM member;

/*
Round(컬럼명, 반올림할 자릿수) 함수 : 반올림 함수
- 반올림은 반올림할 자릿수 밑에서 반올림됩니다.
- 0의 자릿수는 소숫점 위치를 의미합니다.
*/
SELECT 1234.5678 AS orgNo,
		 ROUND(1234.5678, 0) AS N01,
		 ROUND(1234.5678, 1) AS N01,
		 ROUND(1234.5678, -1) AS N01;
		 
/*
회원중에 취미가 수영인 회원이 구매한 상품들을 조회하려고 합니다
회원 지역이 서울, 대전, 광주이며,
상품분류명 중에 피혁이라는 분류에 속해있는 상품을 구매한 회원에 대한
상품명, 상품 분류명, 원가(소숫점 2자리까지 표시)를 조회해 주세요
단, 원가 = 매입가/판매가의 백분율 입니다.
원가 = ROUND(prod_cost/prod_sale, 2) 
member, lprod, prod
*/		 
SELECT prod_name, (SELECT lprod_nm FROM lprod WHERE lprod_gu = prod_lgu) AS lprod_name, ROUND(prod_cost/prod_sale * 100, 2) AS cost
FROM prod
WHERE prod_id IN(SELECT cart_prod FROM cart WHERE cart_member 
						IN(SELECT mem_id FROM member WHERE mem_like = '수영'
																AND SUBSTRING(mem_add1, 1, 2) IN('서울','대전','광주')))		 
               AND prod_lgu IN (SELECT lprod_gu FROM lprod WHERE SUBSTRING(lprod_nm,1,2) = '피혁');
               
/*
<Case 문>
- 문법
	: Case 조건값 When 값 Then 처리로직 Else 처리로직 End;
	: Case When 조건식 Then 처리로직 Else 처리로직 End;
*/
SELECT(Case 1 when 1 then '1입니다.' when 0 then '0입니다.' ELSE '뭐지?' End) AS temp_value;
		   
SELECT(Case when 1 > 0 then '1입니다.' when 1 < 0 then '0입니다.' ELSE '뭐지?' End) AS temp_value;
		 		 
/*
<Case 문>
회원아이디, 회원이름, 성별 조회하기
*/		 
SELECT mem_id, mem_name, SUBSTRING(mem_regno2,1,1) AS regno,
								 (Case SUBSTRING(mem_regno2,1,1) when 1 then '남성'
								 											when 3 then '남성' 
								 											when 2 then '여성' 
																			when 4 then '여성'ELSE '뭐지?' END) AS mf
									
FROM member;		

/*
회원아이디, 회원이름, 성별, 등급 조회하기
- 등급은 마일리지의 값이 5000이상이면 우수고객, 미만은 일반고객으로 구분하여 조회
*/		 
SELECT mem_id, mem_name, SUBSTRING(mem_regno2,1,1) AS regno,
								 (Case SUBSTRING(mem_regno2,1,1) when 1 then '남성'
								 											when 3 then '남성' 
								 											when 2 then '여성' 
																			when 4 then '여성' ELSE '뭐지?' END) AS mf,
								mem_mileage, (case when mem_mileage >= 5000 then '우수고객' ELSE '일반고객' END)	AS level										
									
FROM member;

/*
IF(조건식, 참일때처리, 거짓일때처리) 함수
*/		
SELECT if(10 > 100, '크다', '작다') ifval;

/*
회원이름, 성별 조회하기(if 함수 사용)
*/		
SELECT mem_name, SUBSTRING(mem_regno2,1,1) AS mf1,
								 if (SUBSTRING(mem_regno2,1,1) IN (1, 3), '남자', '여자') AS mf									
FROM member;

/*
Null(결측치) 체크
- IS NULL : NULL인 조건
- IS NOT NULL : NULL이 아닌 조건
- NULL인 경우 : 값을 INSERT 시에 값을 입력 안한 경우(공간이 존재하지 않음)
- NULL이 아닌 경우 : INSERT 시에 '' 이렇게 값을 입력 경우 NULL이 아님(공간이 존재함)
*/		
-- IS NULL, IS NOT NULL 은 국제 표준 입니다.
SELECT*								
FROM prod
WHERE prod_mileage IS NULL;
-- WHERE prod_mileage IS NOT NULL;

/*
널(Null, 결측치) 데이터 대체하기
- IFNULL(컬럼명, Null일 경우 대체값)함수 사용
	: 컬럼값이 null이 아니면 자기자신값 출력,
					null이면 대체값으로 출력
*/	
-- nvl() 널을 대체하는 함수_주로 사용됨
SELECT prod_name, IFNULL(prod_mileage, 0) AS nullnum, nvl(prod_mileage, 0)								
FROM prod;
 
/*
<그룹(집계) 함수>
- 국제 표준을 따릅니다.
- count(), sum(), min(), max(), avg() 5개의 집계함수가 존재합니다.
- sum 또는 avg를 사용할 경우에는 null체크를 꼭 해야합니다.
	ex) sum(nvl(값, 0)), avg(nvl(값, 0))
*/	
 
/*
회원정보 전체에 대한 집계 정보 조회하기
- 회원 총수, 마일리지(총합, 최소값, 최대값, 평균값) 조회하기
*/	
SELECT COUNT(*), sum(nvl(mem_mileage, 0)), MIN(nvl(mem_mileage, 0)), MAX(nvl(mem_mileage, 0)), AVG(nvl(mem_mileage, 0))						
FROM member;
 
/*
서울, 대전, 부산에 거주하는 회원들에 대한
- 회원 총수, 마일리지(총합, 최소값, 최대값, 평균값) 조회하기
-> 해당 조건에 만족하는 전체 집계 결과는 1개 행
*/	 
SELECT COUNT(*), COUNT(mem_id), sum(nvl(mem_mileage, 0)), MIN(nvl(mem_mileage, 0)), MAX(nvl(mem_mileage, 0)), AVG(nvl(mem_mileage, 0))
FROM member
WHERE SUBSTRING(mem_add1, 1, 2) IN ('서울', '대전', '부산');
 
/*
전체 집계가 아닌, 소그룹 집계(범주별 집계)
- 지역별 회원들의 정보를 집계해주세요.
- 지역명, 지역별 회원수, 마일리지(총합, 최솟값, 최댓값, 평균값) 조회하기

-- > 집계함수와 일반함수(또는 일반컬럼)을 함께 조회하는 경우에는
		일반함수(또는 일반컬럼)은 무조건 Group BY 절에 작성해야 합니다_사용안하면 오류남
*/	  
SELECT SUBSTRING(mem_add1, 1, 2) AS AREA, mem_like,
		 COUNT(*), COUNT(mem_id), sum(nvl(mem_mileage, 0)), MIN(nvl(mem_mileage, 0)), MAX(nvl(mem_mileage, 0)), AVG(nvl(mem_mileage, 0))
FROM member
GROUP BY SUBSTRING(mem_add1, 1, 2), mem_like;

/*
그룹조건 : Havig 절에 그룹조건을 제시
			: 그룹조건은 집계함수를 이용한 조건을 의미함
			: Group by절 다음에 작성

그룹이 이루어진 정렬(Order by)의 경우에는 
Select절 뒤에 사용된 컬럼들(별칭) 또는 Group by절 뒤에 사용된 컬럼들만
정렬로 사용할 수 있습니다.
*/
SELECT SUBSTRING(mem_add1, 1, 2) AS AREA, mem_like,
		 COUNT(*), COUNT(mem_id), sum(nvl(mem_mileage, 0)), MIN(nvl(mem_mileage, 0)), MAX(nvl(mem_mileage, 0)), AVG(nvl(mem_mileage, 0))
FROM member
-- 일반 조건절
WHERE SUBSTRING(mem_add1, 1, 2) IN ('서울', '대전', '부산')
-- 그룹(집계)
GROUP BY SUBSTRING(mem_add1, 1, 2), mem_like
-- 그룹(집계) 조건
HAVING COUNT(mem_id) >= 2
ORDER BY mem_like ASC;  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
		 
		 