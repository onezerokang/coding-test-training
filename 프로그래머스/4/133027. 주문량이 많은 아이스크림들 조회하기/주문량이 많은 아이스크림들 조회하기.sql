# 상반기 주문정보: FIRT_HALF - SHIPMENT_ID(FK), FLAVOR(PK), TOTAL_ORDER
# 7월 주문 정보: JULY - SHIPMENT_ID(PK), FLAVOR(FK), TOTAL_ORDER
# 7월에는 아이스크립 주문량이 많아, 같은 맛이어도 다른 출하번호를 갖게 될 수 있음
# 7월 아이스크림 총 주문량, 상반기 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL

# JOIN과 GROUP BY를 둘다 써야할 것 같다.
# 상반기는 6월까지고, JULY는 7월까지라서 그둘을 합친 총 주문량을 더한 값이 큰 순서대로 조회하라는 거군..

SELECT F.FLAVOR
FROM FIRST_HALF F
    INNER JOIN JULY J
    ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY SUM(F.TOTAL_ORDER + J.TOTAL_ORDER) DESC
LIMIT 3;