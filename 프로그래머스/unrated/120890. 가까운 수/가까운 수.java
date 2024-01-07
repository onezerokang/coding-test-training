
import java.util.*;

class Solution {
    public int solution(int[] array, int n) {
        int minAbs = Integer.MAX_VALUE;
        int result = Integer.MAX_VALUE;
        
        for (int num: array) {
            int abs = Math.abs(n - num);
            
            if (minAbs == abs && result > num) {
                result = num;
            }
            
            if (minAbs > abs) {
                minAbs = abs;
                result = num;
            }
        }
        
        return result;
    }
}