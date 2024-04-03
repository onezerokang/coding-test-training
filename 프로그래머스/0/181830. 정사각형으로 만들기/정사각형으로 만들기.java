import java.util.*;

class Solution {    
    private List<List<Integer>> arrayToList(int[][] arr) {
        List<List<Integer>> square = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < arr[i].length; j++) {
                row.add(arr[i][j]);
            }
            square.add(row);
        }
        return square;
    }
    
    private int[][] listToArray(List<List<Integer>> list) {
        int rowSize = list.size();
        int columnSize = list.get(0).size();
        int[][] arr = new int[rowSize][columnSize];
        for (int i = 0; i < rowSize; i++) {
            for (int j = 0; j < columnSize; j++) {
                arr[i][j] = list.get(i).get(j);
            }
        }        
        
        return arr;
    }
    
    public int[][] solution(int[][] arr) {
        int rowCount = arr.length;
        int columnCount = arr[0].length;
        
        if (rowCount == columnCount) {
            return arr;
        }
        
        List<List<Integer>> square = arrayToList(arr);
        
        if (columnCount > rowCount) {
            List<Integer> tmp = new ArrayList<>();
            for (int i = 0; i < columnCount - rowCount; i++) {
                for (int j = 0; j < columnCount; j++) {
                    tmp.add(0);
                }
                square.add(tmp);
            }
        }
        
        if (rowCount > columnCount) {
            for (int i = 0; i < rowCount; i++) {
                for (int j = 0; j < rowCount - columnCount; j++) {
                    square.get(i).add(0);
                }
            }
        }
        
        return listToArray(square);
    }
}
