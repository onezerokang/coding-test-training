import java.util.*;

class Solution {
    private static final List<Move> moves = new ArrayList<>();
    
    private static class Move {
        public final int start;
        public final int end;
        
        public Move(int start, int end) {
            this.start = start;
            this.end = end;
        }
        
        public int[] toArray() {
            return new int[]{this.start, this.end};
        }
    }
    
    public void move(int n, Move move) {
        final int start = move.start;
        final int end = move.end;
        if (n == 1) {
            moves.add(new Move(start, end));
            return;
        }
        
        // 전반부: 1 ~ n-1번째의 원판을 end가 아닌 곳으로 옮기기
        move(n - 1, new Move(start, 6 - start - end));
        
        // 중반부: n번째 원판을 end로 옮기기
        moves.add(new Move(start, end));
        
        // 후반부: 1 ~ n-1번째 원판을 end로 옮기기
        move(n - 1, new Move(6 - start - end, end));
    }
    
    public int[][] solution(int n) {
        move(n, new Move(1, 3));
        
        int[][] result = new int[moves.size()][2];
        int index = 0;
        for (Move move: moves) {
            result[index++] = move.toArray();
        }
        
        return result;
    }
}
