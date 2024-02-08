class Solution {
    public String solution(String my_string, int[] index_list) {
        StringBuilder builder = new StringBuilder();
        for (int index: index_list) {
            builder.append(my_string.charAt(index));
        }
        
        return builder.toString();
    }
}