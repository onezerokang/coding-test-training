import java.util.*;

class Solution {
    private List<String> split(String s, int unit) {
        List<String> tokens = new ArrayList<>();
        for (int startIndex = 0; startIndex < s.length(); startIndex += unit) {
            int endIndex = startIndex + unit;
            if (endIndex >= s.length()) {
                endIndex = s.length();
            }
            tokens.add(s.substring(startIndex, endIndex));
        }
        
        return tokens;
    }
    
    private int compress(String s, int unit) {
        StringBuilder builder = new StringBuilder();
        String last = "";
        int count = 0;
        
        for (String token: split(s, unit)) {
            if (token.equals(last)) {
                count++;
            } else {
                if (count > 1) {
                    builder.append(count);
                }
                builder.append(last);
                last = token;
                count = 1;
            }
        }
        
        if (count > 1) {
            builder.append(count);
        }
        builder.append(last);
        return builder.length();
    }
    
    public int solution(String s) {
        int result = Integer.MAX_VALUE;
        for (int i = 1; i <= s.length(); i++) {
            result = Math.min(result, compress(s, i));
        }
        
        return result;
    }
}