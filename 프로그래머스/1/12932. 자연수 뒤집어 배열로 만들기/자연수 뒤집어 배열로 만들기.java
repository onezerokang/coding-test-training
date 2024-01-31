class Solution {
    public int[] solution(long n) {
        String reversedNum = new StringBuilder(Long.toString(n)).reverse().toString();
        
        int[] result = new int[reversedNum.length()];
        for (int i = 0; i < reversedNum.length(); i++) {
            result[i] = reversedNum.charAt(i) - '0';
        }
        
        return result;
    }
}