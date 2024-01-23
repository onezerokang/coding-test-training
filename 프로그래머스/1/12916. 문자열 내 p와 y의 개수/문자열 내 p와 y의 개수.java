class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        
        int pCount = 0;
        int yCount = 0;
        for (char c: s.toCharArray()) {
            switch (c) {
                case 'p':
                    pCount += 1;
                    break;
                case 'y':
                    yCount += 1;
                    break;
            }
        }
        
        return pCount == yCount;
    }
}

// p 개수와 y 개수가 같으면 true
// 하나도 없으면 true
// 대소문자는 구별하지 않는다.

// s를 대문자/소문자로 통일한다.
// 하나씩 카운트하면서 s와 p 개수를 카운팅
// 같으면 true 아니면 false