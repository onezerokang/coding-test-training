import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[][] triangle = getTriangle(n);
        
        int x = 0;
        int y = 0;
        int value = 1;
        boolean up = false;
        
        while(true) {
            triangle[y][x] = value;
            value += 1;
            
            if (n == 1) {
                break;
            }
                        
            if (!up && triangle.length > y + 1 && triangle[y+1][x] == 0) {
                // 값을 채우고, 내 밑에 뭐가 있다면 내려가서 채운댜.
                y += 1;
                continue;
            }
            
            if (!up && triangle[y].length > x + 1 && triangle[y][x+1] == 0) {
                // 값을 채우고, 내 밑에 뭐가 없다면 오른쪽으로 간다.
                x += 1;
                continue;
            }
            
            if (triangle[y - 1][x - 1] == 0) {
                // 값을 채우고, 내 밑과 오른쪽에 뭐가 없다면 위로 간다.
                y -= 1;
                x -= 1;
                up = true;
                continue;
            }
            
            if (triangle.length > y + 1 && triangle[y+1][x] == 0) {
                // 값을 채우고, 내 밑에 뭐가 있다면 내려가서 채운댜.
                y += 1;
                up = false;
                continue;
            }
            
            break;
        }
        
        List<Integer> list = new ArrayList<>();
        
        for (int[] row: triangle) {
            for (int num: row) {
                list.add(num);
            }
        }
        
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }
        
        return result;
    }
    
    private int[][] getTriangle(int height) {
        int[][] triangle = new int[height][];
        
        for (int i = 0; i < height; i++) {
            triangle[i] = new int[i + 1];
        }
        
        return triangle;
        
    }
}

