/*
<조인(관계, join)>
- 조인 종류 : Inner Join, Left Outer Join, Right Outer Join, Self Join, Natural Join
				: Inner Join, Outer Join, Self Join
				: Cross Join (사용하지 않습니다. 관계조건식이 없는 조인)
*/

/*
<Inner Join>
- 부모와 자식간의 테이블 관게에서
	PK와 FK가 같은 경우에만 조회시키는 경우
- From 절에 사용할 테이블을 모두 제기해서 사용가능
- PK와 FK가 같은 경우를 관계조건(PK컬럼명 = FK컬럼명)으로 작성합니다.
- 국제 표준 방식과 일반 방식 모두 사용가능하며, 
	국내에서는 주로 일반 방식으로 사용합니다.
	외국에서는 국제 표준 방식을 주로 사용합니다.
*/

/*
회원아이디, 이름, 주문 상품 코드, 주문 수량을 조회
*/
-- 일반 방식
SELECT mem_id, mem_name, cart_prod, cart_qty
FROM member, cart, prod,
-- 관계 조건식(PK = FK)
WHERE mem_id = cart_member AND cart_prod = prod_id;

-- 국제 표준 방식
SELECT mem_id, mem_name, cart_prod, cart_qty
FROM member INNER Join cart ON(mem_id = cart_member)
										-- 일반 조건이 있는 경우
										-- AND 컬럼명 >= 값
				Inner Join prod ON(cart_prod = prod_id);

/*
관계조건식 갯수 = 테이블 갯수 - 1
- 최소 갯수 입니다.
*/
-- 28개 행
SELECT COUNT(*) FROM member;
-- 135개 행
SELECT COUNT(*) FROM cart;
-- 3780
SELECT 28 * 135;

SELECT COUNT(*) FROM member, cart;

/*
상품명에 삼성이 포함되어 있는 상품을 구매한 
회원 아이디, 회원이름, 상품명을 조회하려고 합니다.
정렬은 회원이름 기준 오름차순
일반방식과 국제표준방식으로 작성
*/
-- 일반 방식
SELECT mem_id, mem_name, prod_name
FROM member, cart, prod
WHERE mem_id = cart_member AND cart_prod = prod_id AND prod_name LIKE '%삼성%'
ORDER BY mem_name ASC;

-- 국제 표준 방식
SELECT mem_id, mem_name, prod_name
FROM member INNER Join cart ON(mem_id = cart_member)
				INNER Join prod ON(cart_prod = prod_id AND prod_name LIKE '%삼성%')
ORDER BY mem_name ASC;
	
/*
회원별 구매금액의 총액을 조회하려고 합니다.
조회컬럼은 회원이름, 구매금액의 총액
단, 2005년 5월에 주문한 내역에 대해서 처리합니다.(주문번호의 앞자리 8자리는 년월일을 의미)
구매금액 = 주문수량 * 판매가격
ROUND(prod_aty * prod_sale) AS cost
*/
-- 일반방식
SELECT mem_name, cart_no, SUM(nvl(cart_qty * prod_sale, 0)) AS cost
FROM member, cart, prod
WHERE mem_id = cart_member AND cart_prod = prod_id AND SUBSTRING(cart_no,1,6) = '200505'
GROUP BY mem_name
ORDER BY cost ASC;

-- 표준방식 				
SELECT mem_name, cart_no, SUM(nvl(cart_qty * prod_sale, 0)) AS cost
FROM member INNER JOIN cart ON(mem_id = cart_member AND SUBSTRING(cart_no,1,6) = '200505')
            INNER JOIN prod ON(cart_prod = prod_id)
GROUP BY mem_name
ORDER BY cost ASC;

/*
회원아이디, 회원이름, 주문수량, 상품명 조회하기
단, 구매 상품의 거래처 주소가 서울, 대전, 부산인 경우
		상품분류명에 '전자'가 포함된 경우
		주문수량이 5이상인 경우
정렬은 아이디 오름차순, 주문수량 내림차순
-- 일반방식, 표준방식 각각 작성
*/
-- 일반방식
SELECT mem_id, mem_name, prod_name, cart_qty, lprod_nm
FROM member, cart, prod, buyer, lprod
WHERE mem_id = cart_member AND cart_prod = prod_id AND buyer_lgu = lprod_gu and lprod_nm LIKE '%전자%' AND cart_qty >= 5
		AND buyer_id = prod_buyer AND SUBSTRING(buyer_add1,1,2) IN ('서울', '대전', '부산')
ORDER BY mem_id ASC, cart_qty DESC;

-- 표준방식 	
SELECT mem_id, mem_name, prod_name, cart_qty, lprod_nm
FROM member INNER JOIN cart ON(mem_id = cart_member AND cart_qty >= 5)
				INNER JOIN prod ON(cart_prod = prod_id) 
				INNER JOIN buyer ON(prod_buyer = buyer_id AND SUBSTRING(buyer_add1,1,2) IN ('서울', '대전', '부산'))
				INNER JOIN lprod ON(lprod_gu = buyer_lgu AND lprod_nm LIKE '%전자%') AND lprod_nm LIKE '%전자%'
ORDER BY mem_id ASC, cart_qty DESC;
		
/*
<Outer join>
- 선행조건 : Inner Join을 만족해야함(관계 조건식 그대로 적용)
- 다만, 일반방식으로 사용할 수 없음(일반 방식은 관계가 있는, 즉 PK와 FK의 값이 서로 있는 경우만 가능)
- PK와 FK의 값이 서로 없는 경우에도 조회할때 사용되는 Join 방식
- 조회할 컬럼의 경우 널 체크가 필요한 경우 NVL()함수를 사용하여 Null처리를 해야함
- 보통 전체에 대한 현황 분석(통계, 집계)시에 사용되는 Join 방식
- Left Outer Join과 Right Outer Join 방식이 있으며, Left 방식을 주로 사용함
- 오라클(Oracle) DB의 경우 Full Outer Join 방식이 있으나, 사용되는 경우는 거의 없음
- Pandas의 데이터프레임(Dataframe)에서 Merge()함수 사용시 how = left or how = right 와 동일
*/	
	
/*
회원별 구매금액의 총합을 조회해 주세요
 구매금액 = 주문수량 * 판매 단가
*/		
-- 일반 방식
SELECT mem_name, prod_sale, cart_qty, SUM(prod_sale * cart_qty) AS price
FROM member, cart, prod
WHERE mem_id = cart_member AND cart_prod = prod_id
GROUP BY mem_name;	

-- 표준 방식
SELECT mem_name, prod_sale, cart_qty, SUM(prod_sale * cart_qty) AS price
FROM member INNER JOIN cart ON(mem_id = cart_member)
				INNER JOIN prod ON(cart_prod = prod_id)
GROUP BY mem_name;	
		
/*
회원 전체에 대해서 구매금액의 현황을 죄회하려고 합니다.
- 회원이름, 구매금액의 합 조회
- 조건, 회원의 거주 지역이 서울 대전 부산인 경우
*/
SELECT COUNT(*) 
FROM member;

-- 표준 방식
SELECT mem_name, prod_sale, cart_qty, SUM(nvl(prod_sale * cart_qty, 0)) AS price
FROM member LEFT OUTER JOIN cart ON(mem_id = cart_member AND SUBSTRING(mem_add1,1,2) IN ('서울', '대전', '부산'))
				LEFT OUTER JOIN prod ON(cart_prod = prod_id)
# WHERE SUBSTRING(mem_add1,1,2) IN ('서울', '대전', '부산')
GROUP BY mem_name;	
		
/*
상품분류 전체에 대한 상품종류가 몇개씩 있는지 집계해 주세요
- 조회컬럼, 상품분류코드, 상품분류명, 상품건수
- 정렬은 상품건수를 기준으로 내림차순
*/
SELECT lprod_gu, lprod_nm, COUNT(prod_lgu) AS cnt
FROM lprod LEFT OUTER JOIN prod ON(lprod_gu = prod_lgu)
GROUP BY lprod_gu, lprod_nm
ORDER BY cnt DESC;

SELECT lprod_gu, lprod_nm, COUNT(prod_lgu) AS cnt
FROM lprod RIGHT OUTER JOIN prod ON(lprod_gu = prod_lgu)
GROUP BY lprod_gu, lprod_nm
ORDER BY cnt DESC;

/*
2005년도에 주문된 상품에 대한 월별 판매현황을 조회하려고 합니다.
- 조회컬럼 : 주문 월, 월별 총 주문 수량, 월별 총 구매 금액
- 구매금액 = 주문 수량 * 판매 가격
*/
SELECT SUBSTRING(cart_no,5,2) AS MONTH, SUM(nvl(cart_qty,0)) AS qty_cnt, SUM(nvl(prod_sale * cart_qty,0)) AS sale   
FROM cart LEFT OUTER JOIN prod ON(cart_prod = prod_id AND SUBSTRING(cart_no,1,4) = '2005')
GROUP BY MONTH;

/*
회원아이디 b001 회원의 마일리지보다 큰 회원들을 조회
- 조회컬럼 : 아이디, 이름, 마일리지
*/
SELECT mem_id, mem_name, mem_mileage
FROM member
WHERE mem_mileage > (SELECT mem_mileage FROM member WHERE mem_id = 'b001');
---
SELECT mem_id, mem_name, mem_mileage, (SELECT mem_mileage FROM member WHERE mem_id = 'b001') AS boo1_mi
FROM member
WHERE mem_mileage > (SELECT mem_mileage FROM member WHERE mem_id = 'b001');
--- 
SELECT mem_id, mem_name, member.mem_mileage
FROM member, (SELECT mem_mileage FROM member WHERE mem_id = 'b001') as MEM
WHERE member.mem_mileage > MEM.mem_mileage;

-- Self join
SELECT M1.mem_id, M1.mem_name, M1.mem_mileage, M2.mem_mileage 
FROM member M1, member M2
WHERE M2.mem_id = 'b001'
AND M1.mem_mileage > M2.mem_mileage;
