import java.util.*;

class Solution {
    public String solution(String s) {
        Character[] arr = new Character[s.length()];
        int i = 0;
        for (char c: s.toCharArray()) {
            arr[i++] = (Character)c;
        }
        
        Arrays.sort(arr, (Character v1, Character v2) -> v2 - v1);
        StringBuilder builder = new StringBuilder();
        for (Character c: arr) {
            builder.append(c);
        }
        return builder.toString();
    }
}