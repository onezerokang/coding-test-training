import java.util.*;

class Solution {
    public int solution(int[][] lines) {        
        int[] arr1 = compareLines(lines[0], lines[1]);
        int[] arr2 = compareLines(lines[0], lines[2]);
        int[] arr3 = compareLines(lines[1], lines[2]);
        
        int[] result = new int[201];
        fillLine(result, arr1);
        fillLine(result, arr2);
        fillLine(result, arr3);
        
        int answer = 0;
        for (int num: result) {
            if (num == 1) answer++;
        }
        
        return answer;
    }
    
    private int[] compareLines(int[] line1, int[] line2) {
        int[] result = new int[2];
        if (line1[1] > line2[0]) {
            result[0] = Math.max(line1[0], line2[0]);
            result[1] = Math.min(line1[1], line2[1]);
        }
        
        return result;
    }
    
    private void fillLine(int[] result, int[] line) {
        for (int i = line[0] + 100; i < line[1] + 100; i++) {
            result[i] = 1;
        }
    }
}