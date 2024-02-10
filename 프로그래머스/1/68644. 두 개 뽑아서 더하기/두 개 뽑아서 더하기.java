import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers.length; j++) {
                if (i == j) continue;
                set.add(numbers[i] + numbers[j]);
            }
        }
        
        int[] result = set.stream().mapToInt(i -> i).toArray();
        Arrays.sort(result);
            
        return result;
    }
}

// 두 개 수를 뽑아 만들 수 있는 모든 수를 배열에 오름차순으로 담아 solutioion 함수 완성

