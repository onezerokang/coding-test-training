import java.util.*;

class Solution {
    private int[] cutArray(int[] arr, int startIndex, int endIndex) {
        int[] cuttedArr = new int[endIndex - startIndex + 1];
        int index = 0;
        for (int i = 0; i < arr.length; i++) {
            if (i > endIndex) break;
            if (i >= startIndex) cuttedArr[index++] = arr[i];
        }
        return cuttedArr;
    }
    
    public int[] solution(int[] array, int[][] commands) {
        int[] result = new int[commands.length];
        
        for (int index = 0; index < commands.length; index++) {
            int i = commands[index][0];
            int j = commands[index][1];
            int k = commands[index][2];
            
            int[] cuttedArr = cutArray(array, i - 1, j - 1);
            
            Arrays.sort(cuttedArr);
            
            result[index] = cuttedArr[k - 1];
        }
        
        return result;
    }
}