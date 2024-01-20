import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String, Integer> map = new HashMap<>();
        
        // hashmap의 key로 전화번호를 모두 넣는다.
        for (int i = 0; i < phone_book.length; i++) {
            map.put(phone_book[i], i);
        }
        
        // phone_book을 순회한다.
        for (String phone: phone_book) {
            for (int i = 0; i < phone.length(); i++) {
                if (map.containsKey(phone.substring(0, i))) return false;
            }
        }
        
        return true;        
    }
}
