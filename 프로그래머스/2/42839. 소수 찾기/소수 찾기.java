import java.util.*;

class Solution {
    private boolean isPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
    
    private void getPrimes(
        Set<Integer> acc, String numbers, List<Character> others) {
        if (isPrime(Integer.parseInt(numbers))) acc.add(Integer.parseInt(numbers));
        if (others.isEmpty()) return;
        
        for (Character next: others) {
            List<Character> nextOthers = new ArrayList<>(others);
            nextOthers.remove(next);
            getPrimes(acc, numbers + next, nextOthers);
        }
        
    }
    
    public int solution(String numbers) {
        Set<Integer> set = new HashSet<>();
        List<Character> others = new LinkedList<>();
        for (Character c: numbers.toCharArray()) {
            others.add(c);
        }
        
        getPrimes(set, "0", others);
        return set.size();
    }
}

// 상태
// (이어붙인숫자, 선택가능숫자)

// 종료조건
// (이어붙인숫자, empty) -> List<Integer>

// 점화식
// (이어붙인숫자, 선택가능숫자) = (이어붙인숫자, 선택가능숫자) + (이어붙인숫자, 선택가능숫자)

// 종이조각을 붙여 소수 몇개 만들 수 있음?
// 완전탐색으로 모든 소수 다 구하고 -> 소수인지 검사
