import java.util.*;

class Solution {    
    private static final List<String> operators = List.of("+", "-", "*");
    private static final List<List<String>> operatorCombination = List.of(
        List.of("*", "+", "-"),
        List.of("*", "-", "+"),
        List.of("+", "*", "-"),
        List.of("+", "-", "*"),
        List.of("-", "+", "*"),
        List.of("-", "*", "+")
    );
    
    public long solution(String expression) {
        long answer = 0L;
        for (List<String> operators : operatorCombination) {
            Calculator calculator = new Calculator(expression);
            for (String operator : operators) {
                calculator.calculate(operator);
            }   
            answer = Math.max(answer, calculator.getResult());
        }
        
        return answer;
    }
    
    private static class Calculator {
        private List<String> expression = new ArrayList<>();
        private List<String> result = new ArrayList<>();
        
        public Calculator(String expression) {
            int operatorIndex = -1;
            for (int i = 0; i < expression.length(); i++) {
                if (isOperator(expression.charAt(i))) {
                    this.expression.add(expression.substring(operatorIndex + 1, i));
                    this.expression.add(String.valueOf(expression.charAt(i)));
                    operatorIndex = i;
                }
            }
            this.expression.add(
                expression.substring(operatorIndex + 1, expression.length())
            );
        }
        
        private void calculate(String operator) {
            int index = 0;
            while (true) {
                if (operator.equals(expression.get(index))) {
                    long tmp = calculate(
                        expression.get(index),
                        Long.valueOf(result.get(result.size() - 1)),
                        Long.valueOf(expression.get(index + 1))
                    );
                    result.remove(result.size() - 1);
                    result.add(String.valueOf(tmp));
                    index++;
                } else {
                    result.add(expression.get(index));
                }
                if (++index >= expression.size()) {
                    break;
                }
            }
            this.expression.clear();
            this.expression.addAll(this.result);
            this.result.clear();
        }
        
        private long calculate(String operator, long num1, long num2) {
            return switch(operator) {
                case "+" -> num1 + num2;
                case "-" -> num1 - num2;
                case "*" -> num1 * num2;
                default -> throw new RuntimeException("NotAllowedOperator");
            };
        }
        
        public long getResult() {
            return Math.abs(Long.valueOf(expression.get(0)));
        }
        
        
        private boolean isOperator(Character value) {
            return operators.contains(String.valueOf(value));
        }
    }
}