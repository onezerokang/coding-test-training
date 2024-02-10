import java.util.stream.*;
import java.util.*;

class Solution {
    private boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    private Set<Integer> getPrimes(int acc, List<Integer> numbers) {
        Set<Integer> set = new HashSet<>();
        if (isPrime(acc)) {
            set.add(acc);
        }
    
        for (int i = 0; i < numbers.size(); i++) {
            int nextAcc = acc * 10 + numbers.get(i);
            List<Integer> copiedNumbers = new ArrayList<>(numbers);
            copiedNumbers.remove(i);
            set.addAll(getPrimes(nextAcc, copiedNumbers));
        }
        
        return set;
    }
    
    public int solution(String numbers) {
        List<Integer> nums = numbers.chars()
            .map(c -> c - '0')
            .boxed()
            .collect(Collectors.toList());
        return getPrimes(0, nums).size();
    }
}