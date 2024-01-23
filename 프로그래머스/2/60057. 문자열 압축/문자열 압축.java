import java.util.*;

class Solution {
    // 설정된 길이만큼 문자열을 잘라낸 token 배열 생성
    private List<String> split(String source, int length) {
        List<String> tokens = new ArrayList<>();
        for (int startIndex = 0; startIndex < source.length(); startIndex += length) {
            int endIndex = startIndex + length;
            if (endIndex > source.length()) endIndex = source.length();
            tokens.add(source.substring(startIndex, endIndex));
        }
        return tokens;
    }   
    
    private int compress(String source, int length) {
        StringBuilder sb = new StringBuilder();
        
        List<String> tokens = split(source, length);
        String last = "";
        int count = 0;
        for (String token: tokens) {
            if (token.equals(last)) {
                count++;
            } else {
                if (count > 1) sb.append(count);
                sb.append(last);
                last = token;
                count = 1;
            }
        }
        
        if (count > 1) sb.append(count);
        sb.append(last);
        
        return sb.length();
    }
    
    public int solution(String s) {
        int min = Integer.MAX_VALUE;
        for (int length = 1; length <= s.length(); length++) {
            // 문자열 압축 후 가장 짧은 길이 선택
            int compressed = compress(s, length);
            if (compressed < min) {
                min = compressed;
            }
        }
        
        return min;
    }
}