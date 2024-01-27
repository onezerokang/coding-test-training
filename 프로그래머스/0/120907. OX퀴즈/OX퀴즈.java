import java.util.*;

class Solution {
    private String checkFormula(int x, int y, int z, String op) {
        if ("+".equals(op)) {
            return x + y == z ? "O" : "X";
        } else {
            return x - y == z ? "O" : "X";           
        }
    }
    
    public String[] solution(String[] quiz) {
        String[] result = new String[quiz.length];
        int index = 0;
        for (String q: quiz) {
            String[] formula = q.split(" ");
            int x = Integer.parseInt(formula[0]);
            String op = formula[1];
            int y = Integer.parseInt(formula[2]);
            String eq = formula[3];
            int z = Integer.parseInt(formula[4]);
            
            result[index++] = checkFormula(x, y, z, op);
        }
        
        return result;
    }
}