import java.util.*;

class Solution {    
    private static class Supo {
        public int no;
        public int count;
        public final int[] pattern;
        
        public Supo(int no, int[] pattern) {
            this.no = no;
            this.pattern = pattern;
        }
        
        public void check(int answer, int index) {
            if (this.pattern[index % pattern.length] == answer) count++;
        }
        
        public static int[] getHighSupo(Supo[] supos) {
            int highScore = Integer.MIN_VALUE;
            List<Integer> list = new ArrayList<>();
            
            for (Supo supo: supos) {
                if (highScore < supo.count) {
                    highScore = supo.count;
                    list.clear();
                    list.add(supo.no);
                    continue;
                }
                if (highScore == supo.count) {
                    list.add(supo.no);
                }
            }
            
            int[] result = new int[list.size()];
            int index = 0;
            for (int supoNo: list) {
                result[index++] = supoNo;
            }
            
            return result;
        }
        
    }
    
    public int[] solution(int[] answers) {
        Supo supo1 = new Supo(1, new int[]{1, 2, 3, 4, 5});
        Supo supo2 = new Supo(2, new int[]{2, 1, 2, 3, 2, 4, 2, 5});
        Supo supo3 = new Supo(3, new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5});
        
        int index = 0;
        for (int answer: answers) {
            supo1.check(answer, index);
            supo2.check(answer, index);
            supo3.check(answer, index);
            index++;
        }
        
        return Supo.getHighSupo(new Supo[]{supo1, supo2, supo3});
    }
}