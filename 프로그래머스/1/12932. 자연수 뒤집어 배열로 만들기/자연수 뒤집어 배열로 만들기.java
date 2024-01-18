import java.util.*;

class Solution {
    public int[] solution(long n) {
        String strN = Long.toString(n);
        
        String reversed = new StringBuilder(strN).reverse().toString();
        
        char[] charArr = reversed.toCharArray();
        
        int[] result = new int[charArr.length];
        for (int i = 0; i < charArr.length; i++) {
            result[i] = Character.getNumericValue(charArr[i]);
        }
        
        return result;
    }
}