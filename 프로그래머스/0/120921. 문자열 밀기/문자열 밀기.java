class Solution {
    public int solution(String A, String B) {
        int count = 0;
        String tmp = A;
        
        while (true) {
            if (tmp.equals(B)) return count;
            if (tmp.length() == count) return -1;
            tmp = pushString(tmp);
            count++;
        }
    }
    
    private String pushString(String str) {
        StringBuilder sb = new StringBuilder();
        sb.append(str.charAt(str.length() - 1));
        for (int i = 0; i < str.length() - 1; i++) {
            sb.append(str.charAt(i));
        }
        
        return sb.toString();
    }
}