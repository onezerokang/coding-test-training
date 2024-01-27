class Solution {
    private int checkBabbling(String babbling) {
        String[] checkList = new String[]{"aya", "ye", "woo", "ma"};
        
        int index = 0;
        while (index < 4) {
            if (babbling.length() == 0) {
                return 1;
            }

            if (babbling.startsWith(checkList[index])) {
                babbling = babbling.replace(checkList[index], "");
                index = 0;
                continue;
            }
            index++;
        }
        
        return 0;
    }
    
    public int solution(String[] babbling) {
        int answer = 0;
        
        for (String b: babbling) {
            answer += checkBabbling(b);
        }
        
        return answer;
    }
}