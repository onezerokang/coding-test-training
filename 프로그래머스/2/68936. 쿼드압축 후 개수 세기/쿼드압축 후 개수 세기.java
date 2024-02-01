class Solution {
    private int[] compress(int[][] arr, int x, int y, int len) {
        // 종료조건1: 한 변의 길이가 1일 경우
        if (len == 1) {
            return arr[y][x] == 0 ? new int[]{1, 0} : new int[]{0 ,1};
        }
        
        int half = len / 2;
        int[] square1 = compress(arr, x, y, half);
        int[] square2 = compress(arr, x + half, y, half);
        int[] square3 = compress(arr, x, y + half, half);
        int[] square4 = compress(arr, x + half, y + half, half);
        
        // 종료조건2: 하위 정사각형들에 0이 하나도 없을 경우
        if (square1[0] == 0 && square2[0] == 0 && square3[0] == 0 && square4[0] == 0) {
            return new int[]{0, 1};
        }
        
        // 종료조건3: 하위 정사각형들에 1이 하나도 없을 경우
        if (square1[1] == 0 && square2[1] == 0 && square3[1] == 0 && square4[1] == 0) {
            return new int[]{1, 0};
        }
        
        int[] result = new int[2];
        result[0] = square1[0] + square2[0] + square3[0] + square4[0];
        result[1] = square1[1] + square2[1] + square3[1] + square4[1];
        
        return result;
    }
        
    public int[] solution(int[][] arr) {
        return compress(arr, 0, 0, arr.length);
    }
}


// 각자 0과 1이 몇개 남았는지를 반환해야 함.

// arr 행의 개수는 1 ~ 1024 이하이며, 2의 거듭 제곱수 형태

// 상태 정의: (x좌표, y좌표, 한변길이)

// 종료 조건: 
// - (x좌표, y좌표, 1) = arr[y좌표][x좌표]

// 점화식
// (x좌표, y좌표, 한변길이) =
// (x좌표, y좌표, 한변길이 / 2) +
// (x좌표 + 한변길이 / 2, y좌표, 한변길이 / 2) +
// (x좌표, y좌표 + 한변길이 / 2, 한변길이 / 2) +
// (x좌표 + 한변길이 / 2, y좌표 + 한변길이 / 2, 한변길이 / 2)

