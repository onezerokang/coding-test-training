import java.util.Arrays;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings);
        Arrays.sort(strings, (String s1, String s2) -> s1.charAt(n) - s2.charAt(n));
        return strings;
    }
}