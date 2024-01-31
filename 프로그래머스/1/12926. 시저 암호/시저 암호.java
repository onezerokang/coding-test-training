class Solution {
    private char push(char c, int n) {
        if (c == ' ') return c;
        
        boolean isUpper = Character.isUpperCase(c);
        char offset = isUpper ? 'A' : 'a';
        int tmp = isUpper ? c - offset : c - offset; 

        return (char)((tmp + n) % 26 + offset);
        
    }
    
    public String solution(String s, int n) {
        StringBuilder builder = new StringBuilder();
        for (char c: s.toCharArray()) {
            builder.append(push(c,n));
        }
        
        return builder.toString();
    }
}

// 알파벳들을 한자씩 민다.
// 끝에 도달하면 처음으로 돌아온다.
// 1. 모든 알파벳 순회
// 1.1. 대문자인지 소문자인지 파악(offset 정하기 위함)
// 1.2. 1 ~ 26 범위내로 들게 하고 n 더하고 26으로 나눈 나머지 구하기
// 1.3. 다시 offset 더함
// 1.4. 복구
// 