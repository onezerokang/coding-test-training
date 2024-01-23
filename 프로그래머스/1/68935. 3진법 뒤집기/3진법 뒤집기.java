class Solution {
    public int solution(int n) {
        String a = Integer.toString(n, 3);
        a = new StringBuilder(a).reverse().toString();
        int b = Integer.parseInt(a, 3);
        return b;
    }
}