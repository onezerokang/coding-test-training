class Solution {
    public String solution(int n) {
        StringBuilder builder = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            builder.append(i % 2 == 0 ? "박" : "수");
        }
        
        return builder.toString();
    }
}