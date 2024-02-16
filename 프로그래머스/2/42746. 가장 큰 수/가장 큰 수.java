import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        List<String> strNumbers = new ArrayList<>();
        for (int n: numbers) {
            strNumbers.add(String.valueOf(n));
        }
        
        Collections.sort(strNumbers, (String s1, String s2) -> {
            return (s2 + s1).compareTo(s1 + s2);
        });
        
        StringBuilder builder = new StringBuilder();
        boolean flag = true;
        for(String str: strNumbers) {
            if (flag && str.equals("0")) continue;
            flag = false;
            builder.append(str);
        }
        
        if (builder.length() == 0) builder.append("0");
        
        return builder.toString();       
    }
}