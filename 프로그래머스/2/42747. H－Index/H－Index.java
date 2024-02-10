class Solution {
    public int solution(int[] citations) {
        for (int h = 1; h <= 1000; h++) {
            int count = 0;
            for (int citation: citations) {
                if (citation >= h) count++;
            }
            if (count < h) return h - 1;
        }
        return 0;
    }
}