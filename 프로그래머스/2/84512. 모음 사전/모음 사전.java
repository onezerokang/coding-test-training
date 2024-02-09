import java.util.*;

class Solution {
    private static final String[] words = {"A", "E", "I", "O", "U"};
    
    private List<String> createDict(String word) {
        List<String> list = new ArrayList<>();
        list.add(word);
        
        if (word.length() == 5) {    
            return list;
        }
        
        for (String w: words) {
            list.addAll(createDict(word + w));
        }
        
        return list;
    }
    
    public int solution(String word) {
        List<String> dict = new ArrayList<>();
        for (String w: words) {
            dict.addAll(createDict(w));
        }
        
        return dict.indexOf(word) + 1;
    }
}