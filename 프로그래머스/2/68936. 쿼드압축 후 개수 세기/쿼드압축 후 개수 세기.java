class Solution {
    private Count compress(Count[] arr) {
        Count result = new Count(0, 0);
        for (Count count: arr) {
            result.zero += count.zero;
            result.one += count.one;
        }
        return result;
    }
    
    private Count compress(int[][] arr, int x, int y, int len) {
        if (len == 1) {
            if (arr[y][x] == 1) {
                return new Count(0, 1);
            } else {
                return new Count(1, 0);
            }
        }
        
        int half = len / 2;
        Count[] compressed = new Count[]{
            compress(arr, x, y, half),
            compress(arr, x + half, y, half),
            compress(arr, x, y + half, half),
            compress(arr, x + half, y + half, half)    
        };
        
        Count result = compress(compressed);
        if (result.zero == 0) return new Count(0, 1);
        if (result.one == 0) return new Count(1, 0);
        return result;
    }
    
    private static class Count {
        int zero;
        int one;
        
        public Count(int zero, int one) {
            this.zero = zero;
            this.one = one;
        }
        
        public int[] toArray() {
            return new int[]{this.zero, this.one};
        }
    }

    
    public int[] solution(int[][] arr) {
        Count count = compress(arr, 0, 0, arr.length);
        return count.toArray();
    }
}

// 최종적으로 남는 0의 개수와 1의 개수를 반환해야 한다.

// 상태 정의
// (x, y, length) -> 해당 정사각형에서 0과 1이 몇개인가

// 종료 조건
// (x, y, length) = [0, 1] -> 1밖에 없거나
// (x, y, length) = [1, 0] -> 0밖에 없음
// (x, y, 1) -> 정사각형 길이가 1임

// 점화식(부분 문제로 현재 문제를 구성), 상태의 전이
// (x, y, length) = 
// (x, y, length / 2) +
// (x + length / 2, y, length / 2) +
// (x, y + length / 2, length / 2) +
// (x + length / 2, y + length / 2, length / 2)