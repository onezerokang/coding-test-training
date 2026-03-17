class Solution {
    fun solution(arr: Array<IntArray>): IntArray {
        return compress(0, 0, arr.size, arr)
    }
    
    fun compress(x: Int, y: Int, len: Int, arr: Array<IntArray>): IntArray {
        val result = intArrayOf(0, 0)
        if (len == 1) {
            result[arr[y][x]] = 1
            return result
        }
        // 모두 같은지 검사
        var countZero: Int = 0
        var countOne: Int = 0
        for (nextX in x until x + len) {
            for (nextY in y until y + len) {
                if (arr[nextY][nextX] == 0) {
                    countZero++
                } else {
                    countOne++
                }
            }
        }
        if (countZero == 0) {
            return intArrayOf(0, 1)
        } else if (countOne == 0) {
            return intArrayOf(1, 0)
        }
        
        // 분할
        val result1 = compress(x, y, len / 2, arr)
        val result2 = compress(x + len / 2, y, len / 2, arr)
        val result3 = compress(x, y + len / 2, len / 2, arr)
        val result4 = compress(x + len / 2, y + len / 2, len / 2, arr)
        
        result[0] = result1[0] + result2[0] + result3[0] + result4[0]
        result[1] = result1[1] + result2[1] + result3[1] + result4[1]
        
        return result
    }
}