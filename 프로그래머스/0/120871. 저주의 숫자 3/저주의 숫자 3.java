import java.util.*;

class Solution {
    private boolean checkThree(int n) {
        return n % 3 == 0 || Integer.toString(n).contains("3");
    }
    
    public int solution(int n) {
        int result = 0;
        for (int i = 1; i <= n; i++) {
            result++;
            while (checkThree(result)) {
                result++;
            }
        }
        
        return result;
    }
}

// 1부터 n번까지 반복한다.
// 숫자에 3이 포함되거나, 3의 배수인 경우 +1을 더한다.
// 더한 값이 위 조건을 충족하지 않을 때까지 더한다.
