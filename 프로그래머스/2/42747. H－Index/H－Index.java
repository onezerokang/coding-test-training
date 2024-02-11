class Solution {
    private boolean isValid(int[] citations, int h) {
        int count = 0;
        for (int citation: citations) {
            if (citation >= h) count++;
        }
        return count >= h;
    }
    
    public int solution(int[] citations) {
        for (int h = citations.length; h >= 1; h--) {
            if (isValid(citations, h)) return h;
        }
        return 0;
    }
    // public int solution(int[] citations) {
    //     for (int h = 1; h <= 1000; h++) {
    //         int count = 0;
    //         for (int citation: citations) {
    //             if (citation >= h) count++;
    //         }
    //         if (count < h) return h - 1;
    //     }
    //     return 0;
    // }
}