class Solution {
    public int[] solution(int brown, int yellow) {
        int[] result = new int[2];
        int totalSize = brown + yellow;
        int w = totalSize;
        int h = 1;
        
        while(h++ <= w) {
            if (totalSize % h != 0) continue;
            w = totalSize / h;
            if (w - 2 <= 0 || h - 2 <= 0) continue;
            if (yellow == (w - 2) * (h - 2)) {
                result = new int[]{w, h};
                break;
            }   
        }
        
        return result;
    }
}
