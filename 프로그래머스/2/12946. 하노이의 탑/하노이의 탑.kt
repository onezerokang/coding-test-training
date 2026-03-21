class Solution {
    fun solution(n: Int): Array<IntArray> {
        return move(n, 1, 3)
    }
    
    fun move(m: Int, start: Int, end: Int): Array<IntArray> {
        if (m == 1) {
            return arrayOf(intArrayOf(start, end))
        }
        
        var result = arrayOf<IntArray>()
        move(m - 1, start, mid(start, end)).forEach { result += it }
        result += intArrayOf(start, end)
        move(m - 1, mid(start, end), end).forEach { result += it }
        return result
    }
    
    fun mid(start: Int, end: Int): Int {
        return when (start + end) {
            5 -> 1
            4 -> 2
            3 -> 3
            else -> 0
        }
        // 1 -> 3 = 2
        // 3 -> 1 = 2
        // 1 -> 2 = 3
        // 2 -> 1 = 3
        // 2 -> 3 = 1
        // 3 -> 2 = 1
    }
}

// 원판 1,2,3을 옮기리면
// 1,2를 먼저 옮기고
// 3을 옮기고
// 1을 옮겨야 한다.


// 원판이 1개면 1번 이동
// 원판이 2개면 3번 이동
// 원판이 3개면 7번 이동
// 원판이 4개면 15번?

// 기둥: [A, B, C]
// 원판: [1, 2, 3, 4]
// 규칙을 지키면서 원판을 기둥C로 옮기려면
// 1~3까지를 B로 옮기고
// 4를 C로 옮긴 후
// 1~3를 C로 옮긴다.

// 원판: [1, 2, 3]
// 1~2까지를 B로 옮기고
// 3를 C로 옮긴 후
// 1~3를 C로 옮긴다.

// 원판: [1, 2]
// 1을 B로 옮기고
// 2를 C로 옮긴 후
// 1를 C로 옮긴다.

// 어떤 반복되는 규칙이 있는가
// 시작지점, 임시지점, 목적지점
// 원판이 n개일 때
// 1~n-1번째 원판을 임시지점에 옮기고
// n번쨰 원판을 목적지점에 올리고
// 1~n-1번째 원판을 목적지점에 올리면 됨.
