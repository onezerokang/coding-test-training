# ANIMAL_INS: 보호소 내부 동물 정보
# ANIMAL_OUTS: 입양 보낸 동물 정보

# 오류 고치기: 보호 시작일이 입양일보다 더 빠른 동물의 아이디와 이름을 조회한다.

SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
    INNER JOIN ANIMAL_OUTS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME > O.DATETIME
ORDER BY I.DATETIME ASC;