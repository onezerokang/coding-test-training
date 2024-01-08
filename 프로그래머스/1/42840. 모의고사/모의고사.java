import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        Supoja supoja1 = new Supoja(1, new int[]{1, 2, 3, 4, 5});
        Supoja supoja2 = new Supoja(2, new int[]{2, 1, 2, 3, 2, 4, 2, 5});
        Supoja supoja3 = new Supoja(3, new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5});
        
        for(int answer: answers) {
            supoja1.checkAnswer(answer);
            supoja2.checkAnswer(answer);
            supoja3.checkAnswer(answer);
        }
        
        List<Integer> ranking = Supoja.getRanking(List.of(supoja1, supoja2, supoja3));
        
        return ranking.stream().mapToInt(i -> i).toArray();
    }
    
    private static class Supoja {        
        private int id;
        private int[] pattern;
        private int patternLength;
        public int correctCount = 0;
        public int currIndex = 0;
        
        public Supoja(int id, int[] pattern) {
            this.id = id;
            this.pattern = pattern;
            this.patternLength = pattern.length;
        }
        
        public void checkAnswer(int answer) {
            if (pattern[currIndex] == answer) {
                correctCount++;
            }
            
            currIndex++;
            
            if (currIndex >= patternLength) {
                currIndex = 0;
            }
        }
        
        public static List<Integer> getRanking(List<Supoja> supojas) {
            int bestScore = 0;
            LinkedList<Integer> ranking = new LinkedList<>();
            
            for (Supoja supoja: supojas) {
                if (bestScore == supoja.correctCount) {
                    ranking.add(supoja.id);
                }

                if (bestScore < supoja.correctCount) {
                    ranking.clear();
                    ranking.add(supoja.id);
                    bestScore = supoja.correctCount;
                }
            }
            
            return ranking;
        }
    }
}