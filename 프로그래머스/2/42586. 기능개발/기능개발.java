import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Deque<Progress> progressQueue = createProgressQueue(progresses, speeds);
        List<Integer> completedTasksPerDay = new LinkedList<>();
        
        while (!progressQueue.isEmpty()) {
            updateAllProgresses(progressQueue);
            int completedTasks = releaseCompletedTasks(progressQueue);
            if (completedTasks > 0) {
                completedTasksPerDay.add(completedTasks);
            }
        }
        
        return completedTasksPerDay.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
    
    private static class Progress {
        int currentProgress;
        int speed;
        
        Progress(int currentProgress, int speed) {
            this.currentProgress = currentProgress;
            this.speed = speed;
        }
        
        void update() {
            this.currentProgress += this.speed;
        }
        
        boolean isCompleted() {
            return this.currentProgress >= 100;
        }
    }

    private Deque<Progress> createProgressQueue(int[] progresses, int[] speeds) {
        Deque<Progress> queue = new ArrayDeque<>();
        for (int i = 0; i < speeds.length; i++) {
            queue.add(new Progress(progresses[i], speeds[i]));
        }
        return queue;
    }
    
    private void updateAllProgresses(Deque<Progress> progressQueue) {
        for (Progress progress : progressQueue) {
            progress.update();
        }
    }
    
    private int releaseCompletedTasks(Deque<Progress> progressQueue) {
        int count = 0;
        while (!progressQueue.isEmpty() && progressQueue.peek().isCompleted()) {
            progressQueue.poll();
            count++;
        }
        return count;
    }
}