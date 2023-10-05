import java.util.*;

// 이전 요소에 값이 없거나, 다른 값이 있으면 요소를 추가한다.
// 그러지 않을 경우 요소를 제거한다.

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        
        for (int num: arr) {
            if (stack.isEmpty() || stack.peek() != num) {
                stack.push(num);
            }
        };        
        
        return stack.stream().mapToInt(Integer::intValue).toArray();
    }
}