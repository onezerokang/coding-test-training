import java.util.*;

class Solution {
    private List<String> split(String source, int length) {
        List<String> tokens = new ArrayList<>();
        for (int startIndex = 0; startIndex < source.length(); startIndex += length) {
            int endIndex = startIndex + length;
            if (endIndex >= source.length()) {
                endIndex = source.length();
            }
            tokens.add(source.substring(startIndex, endIndex));
        }
        return tokens;
    }
    
    private int compress(String source, int length) {
        StringBuilder builder = new StringBuilder();
        String last = "";
        int count = 0;
        for (String token: split(source, length)) {
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
        int minLength = Integer.MAX_VALUE;
        for (int i = 1; i <= s.length(); i++) {
            int compressed = compress(s, i);
            minLength = minLength > compressed ? compressed : minLength;
        }
        return minLength;
    }
}