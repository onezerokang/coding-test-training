class Solution {
    public int[] solution(String s) {
        int[] result = new int[2];
        while (!s.equals("1")) {
            result[0] += 1;
            
            int before = s.length();
            s = s.replaceAll("0", "");
            int after = s.length();
            result[1] += before - after;
            
            s = Integer.toString(s.length(), 2);
        }
        return result;
    }
}

