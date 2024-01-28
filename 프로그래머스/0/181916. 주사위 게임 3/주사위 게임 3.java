import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(a, map.getOrDefault(a, 0) + 1);
        map.put(b, map.getOrDefault(b, 0) + 1);
        map.put(c, map.getOrDefault(c, 0) + 1);
        map.put(d, map.getOrDefault(d, 0) + 1);
        
        List<Integer> keys = new ArrayList<>(map.keySet());
        List<Integer> values = new ArrayList<>(map.values());
        
        if (values.size() == 1) {
            return keys.get(0) * 1111;
        }
        
        if (values.size() == 2 && values.contains(3)) {
            double p = 0;
            double q = 0;
            
            for (int key: keys) {
                if (map.get(key) == 3) p = key;
                else q = key;
            }
            
            return (int) Math.pow(10 * p + q, 2);
            
        }
        
        if (values.size() == 2 && values.contains(2)) {
            int p = keys.get(0);
            int q = keys.get(1);
            return (p + q) * Math.abs(p - q);
        }
        
        if (values.size() == 3) {
            int count = 0;
            int q = 0;
            int r = 0;
            
            for (int key: keys) {
                if (map.get(key) == 1 && count == 0) {
                    q = key;
                    count++;
                } else if (map.get(key) == 1 && count == 1) {
                    r = key;
                }
            }
            
            return q * r;
        }
        

        int min = Integer.MAX_VALUE;
        for (int v: keys) {
            min = Math.min(min, v);
        }
        return min;
        
    }
}