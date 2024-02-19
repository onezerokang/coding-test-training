import java.util.*;

class Solution {
    public String solution(String my_string) {
        Set<Character> set = new LinkedHashSet<>();
        for (char c: my_string.toCharArray()) {
            set.add(c);
        }
        
        StringBuilder builder = new StringBuilder();
        for (char c: set) {
            builder.append(c);   
        }
        return builder.toString();
    }
}