import java.util.*;

class Solution {
    private boolean checkPrime(int n) {
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    public int[] solution(int n) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 2; i <= n; i++) {
            if (checkPrime(i) && n % i == 0) map.put(i, 0);
        }
        
        int[] result = new int[map.size()];
        int index = 0;
        for (int key: map.keySet()) {
            result[index++] = key;
        }
        
        Arrays.sort(result);
        
        return result;
    }
}
