import java.util.*;

class Solution {
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
    
    public int solution(int[][] maps) {
        int maxY = maps.length;
        int maxX = maps[0].length;
        
        int[][] visited = new int[maxY][maxX];
        
        ArrayDeque<Coord> queue = new ArrayDeque<>();
        queue.add(new Coord(0, 0));
        
        while (!queue.isEmpty()) {
            Coord coord = queue.pollFirst();
            int x = coord.getX();
            int y = coord.getY();
            
            for (int i = 0; i < 4; i++) {
                int nx = coord.x + dx[i];
                int ny = coord.y + dy[i];
                
                if (nx == maxX - 1 && ny == maxY - 1) {
                    return visited[y][x] + 2;
                }
                
                if (0 <= nx && nx < maxX && 0 <= ny && ny < maxY && maps[ny][nx] != 0 && visited[ny][nx] == 0) {
                    queue.add(new Coord(nx, ny));
                    visited[ny][nx] = visited[y][x] + 1;
                }
            }
        }       
        
        return -1;
        
    }
    
    private static class Coord {
        private int x;
        private int y;
        
        public Coord(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        private int getX() { return this.x; }
        private int getY() { return this.y; }
    }
}