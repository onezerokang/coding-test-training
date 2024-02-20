# 입양간 기록은 있는데, 보호소에 들어온 기록은 없는 동물의 id와 이름을 id 순으로 조회
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O
    LEFT JOIN ANIMAL_INS I
    ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID ASC;
    