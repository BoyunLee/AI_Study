/*
상품분류정보의 상품분류코드 , 상품분류명 조회하기
단, 상품정보에 상품분류정보가 없는 데이터만 조회하기
*/

SELECT lprod_gu, lprod_nm
FROM lprod WHERE lprod_gu NOT IN (SELECT prod_lgu FROM prod);

/*
서울 또는 대전에 거주하는 회원들이 장바구니에 저장한 데이터를 조회
- 주문번호, 회원아이디,  주문상품코드, 주문수량을 조회
- 주문번호를 기준으로 오름차순
*/

SELECT cart_no, cart_member, cart_prod, cart_qty
FROM cart
WHERE cart_member IN (SELECT mem_id FROM member WHERE substring(mem_add1,1,2)IN('서울','대전'))
ORDER BY cart_no ASC;

/*
상품코드, 상품명, 상품판매가격을 조회
단, 회원의 마일리지 값이 100이상이고,
	 주문수량이 5이상인 상품
	 
	 prod -> cart -> member
*/

SELECT prod_id, prod_name, prod_sale
FROM prod
WHERE prod_id IN (SELECT cart_prod 
						FROM cart
						WHERE cart_qty >=5
						AND cart_member IN (SELECT mem_id 
													FROM member
													WHERE mem_mileage >=100));


/*
상품코드, 상품명, 상품판매가격을 조회
단, 회원의 마일리지 값이 100이상이고,
	 주문수량이 5이상인 상품
	 
추가 조건,...
	상품분류명에 "컴퓨터"라는 단어가 포함되어 있고,
	거래처 주소지가 서울 또는 대전 또는 부산인 경우만 조회
*/

SELECT prod_id, prod_name, prod_sale
FROM prod
WHERE prod_id IN (SELECT cart_prod 
						FROM cart
						WHERE cart_qty >=5
						AND cart_member IN (SELECT mem_id 
													FROM member
													WHERE mem_mileage >=100)) 
and prod_buyer IN (SELECT buyer_id 
						 FROM buyer 
						 WHERE  substring(buyer_add1,1,2)IN('서울','대전','부산')
									and buyer_lgu IN (SELECT lprod_gu 
															FROM lprod 
															WHERE lprod_nm LIKE '%컴퓨터%' )) ;


SELECT prod_id, prod_name, prod_sale
FROM prod
WHERE prod_id IN (SELECT cart_prod 
						FROM cart
						WHERE cart_qty >=5
						AND cart_member IN (SELECT mem_id 
													FROM member
													WHERE mem_mileage >=100)) 
	AND prod_lgu IN (SELECT lprod_gu
						  FROM lprod
						  WHERE lprod_nm LIKE '%컴퓨터%')
	AND prod_buyer IN (SELECT buyer_id
							 FROM buyer
							 WHERE SUBSTRING(buyer_add1,1,2) IN ('서울','대전','부산')) ;

/*
상품코드, 상품명, 상품판매가격, 처래처명 조회
단, 회원의 마일리지 값이 100이상이고, 주문수량이 5이상인 상품
	 
위 조건에 추가하여 다음 조건 처리...
	상품분류명에 "컴퓨터"라는 단어가 포함되어 있고,
	거래처 주소지가 서울 또는 대전 또는 부산인 경우만 조회
*/
SELECT prod_id, prod_name, prod_sale, (SELECT buyer_name FROM buyer WHERE buyer_id = prod_buyer) AS buyer_nm	
FROM (SELECT * FROM prod) A
WHERE prod_id IN (SELECT cart_prod 
						FROM cart
						WHERE cart_qty >=5
						AND cart_member IN (SELECT mem_id 
													FROM member
													WHERE mem_mileage >=100)) 
	AND prod_lgu IN (SELECT lprod_gu
						  FROM lprod
						  WHERE lprod_nm LIKE '%컴퓨터%')
	AND prod_buyer IN (SELECT buyer_id
							 FROM buyer
							 WHERE SUBSTRING(buyer_add1,1,2) IN ('서울','대전','부산'));

/*
<서브쿼리 규칙>
- IN()을 이용하는 경우 : 다중행에 단일컬럼 형태만 조회가능
							  : Where절(조건절) 내에만 사용가능
- = 조건을 이용하는 경우 : 단일행에 단일컬럼 형태만 조회가능
								 : 컬럼명 또는 Where절(조건절)내에 사용가능
- From 뒤에 테이블로 이용하는 경우 : 다중행에 다중컬럼 형태 모두 사용가능
*/







