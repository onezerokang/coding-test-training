import java.util.*;

class Solution { 
    public int solution(int[] nums) {
        
        int limit = nums.length / 2;
        Set<Integer> set = new HashSet<>();
        
        for (int n: nums) {
            set.add(n);
        }
        
        return limit > set.size() ? set.size() : limit;
    }
}