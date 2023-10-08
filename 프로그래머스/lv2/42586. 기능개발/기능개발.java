import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        Deque<List<Integer>> queue = getProgressQueue(progresses, speeds);
        
        List<Integer> result = new LinkedList<>();
        
        while (!queue.isEmpty()) {
            updateProgresses(queue);
            int count = removeCompletedProgresses(queue);
            updateResultIfCountIsAtLeast100(result, count);
        }
        
        return result.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
    
    private Deque<List<Integer>> getProgressQueue(int[] progresses, int[] speeds) {
        Deque<List<Integer>> queue = new ArrayDeque<>();
        for (int i = 0; i < speeds.length; i++) {
            List<Integer> list = new ArrayList<>(2);
            list.add(progresses[i]);
            list.add(speeds[i]);
            queue.add(list);
        }
        return queue;
    }
    
    private void updateProgresses(Deque<List<Integer>> queue) {
        for(List<Integer> list: queue) {
            list.set(0, list.get(0) + list.get(1));
        }
    }
    
    private int removeCompletedProgresses(Deque<List<Integer>> queue) {
        int count = 0;
        while (!queue.isEmpty() && queue.peek().get(0) >= 100) {
            queue.poll();
            count += 1;
        }
        return count;
    }
    
    private void updateResultIfCountIsAtLeast100(List<Integer> result, int count) {
        if (count > 0) {
            result.add(count);
        }
    }
}