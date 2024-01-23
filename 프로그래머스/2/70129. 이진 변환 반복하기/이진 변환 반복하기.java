class Solution {
    private int countZero(String s) {
        int count = 0;
        for (char c: s.toCharArray()) {
            if (c == '0') {
                count++;
            }
        }
        
        return count;
    }
    
    public int[] solution(String s) {
        int[] result = new int[2];
        while (!s.equals("1")) {
            int zeroCount = countZero(s);
            result[0] += 1;
            result[1] += zeroCount;
            s = Integer.toString(s.length() - zeroCount, 2);
        }
        
        
        return result;
    }
}

