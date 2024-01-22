class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();

        for (int c: s.toCharArray()) {
            if (c == ' ') {
                sb.append((char)c);
                continue;
            }
            
            boolean isUpper = Character.isUpperCase(c);
            c += n;
            
            if ((isUpper && c > 'Z') || (!isUpper && c > 'z')) {
                c -= 26;
            }
            
            sb.append((char)c);
        }
        
        return sb.toString();
    }
}