import java.util.*;

class Solution {
    public int solution(int n) {
        List<Integer> divisor = calcDivisor(n);
        return divisor.stream().mapToInt(i -> i).sum();
    }
    
    private List<Integer> calcDivisor(int n) {
        List<Integer> divisor = new LinkedList<>();
        
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                divisor.add(i);
            }
        }
        
        return divisor;
    }
}