class Solution {
    public int solution(int n) {
        String tmp = new StringBuilder(Integer.toString(n, 3)).reverse().toString();
        return Integer.parseInt(tmp, 3);
        
    }
}