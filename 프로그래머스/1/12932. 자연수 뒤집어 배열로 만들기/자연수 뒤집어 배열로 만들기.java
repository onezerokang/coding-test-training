class Solution {
    public int[] solution(long n) {
        StringBuilder builder = new StringBuilder(Long.toString(n));
        builder.reverse();
        String str = builder.toString();
        
        int[] result = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            result[i] = str.charAt(i) - '0';
        }

        return result;
    }
}