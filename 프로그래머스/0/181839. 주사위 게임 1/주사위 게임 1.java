import java.util.*;

class Solution {
    
    private static class GameMachine {
        final int a;
        final int b;
        
        public GameMachine(int a, int b) {
            this.a = a;
            this.b = b;
        }
        
        public int calcScore() {
            if (a % 2 != 0 && b % 2 != 0) {
                return (int)Math.pow(a, 2) + (int)Math.pow(b, 2);
            }
            
            if (a % 2 != 0 || b % 2 != 0) {
                return (a + b) * 2;
            }
            
            return Math.abs(a - b);
        }
    }
    
    public int solution(int a, int b) {
        GameMachine gm = new GameMachine(a, b);
        return gm.calcScore();
    }
}
