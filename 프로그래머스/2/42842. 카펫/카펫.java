import java.util.*;

class Solution {
    // 나올 수 있는 가로 길이, 세로 길이를 모두 구한다.
    //   - 세로 크기는 최소 3이다.
    //   - 총 개수를 3부터 1씩 늘려가면서 나눈다. 딱 나누어떨어지는 경우 가능한 가로*세로이므로 기록한다.
    // 노란색 구하는 공식이 성립하는 가로 * 세로를 구한다.
    //    - (가로길이-2) * (세로길이-2) == 노랑개수 그게 정답.
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        List<List<Integer>> combinations = getWidthHeightCombination(brown + yellow);
        combinations.forEach(widthHeight -> {
            int width = widthHeight.get(0);
            int height = widthHeight.get(1);
            
            if ((width - 2) * (height - 2) == yellow) {
                answer[0] = width;
                answer[1] = height;
            }
        });
        
        
        return answer;
    }
    
    List<List<Integer>> getWidthHeightCombination(int totalCount) {
        Integer height = 3;
        
        List<List<Integer>> result = new ArrayList<>();
        do {
            if (totalCount % height == 0) {
                List<Integer> widthHeight = new ArrayList<>();
                widthHeight.add(totalCount/ height);
                widthHeight.add(height);
                result.add(widthHeight);
            }
            height++;
        } while (totalCount / height >= height);
        return result;
    }
}