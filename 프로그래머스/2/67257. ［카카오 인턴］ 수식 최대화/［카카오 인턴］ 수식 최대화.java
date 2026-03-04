import java.util.*;

class Solution {    
    // 숫자와 연산자를 분리해서 리스트에 담는다.
    // 연산자 우선순위 조합을 구한다.
    // 연산자 우선순위를 순회하면서 합을 구한다.
    // 가장 높은합을 반환한다.
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
                if (operator.equals("+")) {
                    calculator.plus();
                } else if (operator.equals("-")) {
                    calculator.minus();
                } else if (operator.equals("*")) {
                    calculator.multiply();
                }
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
        
        private void plus() {
            int index = 0;
            while (true) {
                if (expression.get(index).equals("+")) {
                    long tmp = Long.valueOf(result.get(result.size() - 1))
                        + Long.valueOf(expression.get(index + 1));
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
        
        private void minus() {
            int index = 0;
            while (true) {
                if (expression.get(index).equals("-")) {
                    long tmp = Long.valueOf(result.get(result.size() - 1))
                        - Long.valueOf(expression.get(index + 1));
                    System.out.println(tmp);
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
        
        private void multiply() {
            int index = 0;
            while (true) {
                if (expression.get(index).equals("*")) {
                    long tmp = Long.valueOf(result.get(result.size() - 1))
                        * Long.valueOf(expression.get(index + 1));
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
        
        public long getResult() {
            return Math.abs(Long.valueOf(expression.get(0)));
        }
        
        
        private boolean isOperator(Character value) {
            return operators.contains(String.valueOf(value));
        }
    }
}