-- 코드를 입력하세요
SELECT P.PRODUCT_ID, PRODUCT_NAME, SUM(PRICE*AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT P JOIN (SELECT PRODUCT_ID, AMOUNT
                     FROM FOOD_ORDER
                     WHERE PRODUCE_DATE LIKE '2022-05%') N
WHERE P.PRODUCT_ID = N.PRODUCT_ID
GROUP BY PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, PRODUCT_ID