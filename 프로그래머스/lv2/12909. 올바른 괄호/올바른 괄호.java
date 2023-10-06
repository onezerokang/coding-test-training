import java.util.*;

class Solution {
    boolean solution(String s) {
        
        Stack<Character> stack = new Stack<>();
        
        for (char c: s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
                continue;
            };
            
            if (stack.isEmpty()) {
                return false;
            }
            
            stack.pop();
        };
        
        return stack.isEmpty();
    }
}