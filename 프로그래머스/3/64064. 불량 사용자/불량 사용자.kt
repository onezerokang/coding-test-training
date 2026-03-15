class Solution {
    // 1. banned_id를 순회하면서 패턴이 일치하는 user_id를 찾고 기록한다.
    // 패턴 일치 검사 방법
    // 1.1. banned_ids를 정규식으로 변경하고 찾는다.
    // 1.2. banned_id와 user_id를 순회하면서 찾는다.
    // { 
    //    "fr*d": ["frodo", "fridi"],
    //    "*rodo": ["frodo", "corodo"],
    //    "******": ["abc123", "frodoc"],
    //    "******": ["abc123", "frodoc"],
    // }
    // 2. 기록된 map을 nested 순회면서 만들어질 수 있는 조합을 리스트에 담는다.
    // 3. 요소가 중복된 리스트는 뺀다.
    
    // 현재 코드의 문제: Map을 사용해서 banned_id와 user_id를 저장했을 때
    //               banned_id가 동일한 값으로 들어올 수 있음.
    // 방법1. IdMap이라는 클래스를 만들어서 처리하고, 리스트에 담는다.
    // [IdMap { banned_id: "*****", user_ids: [""] }]
    
    fun solution(user_id: Array<String>, banned_id: Array<String>): Int {
        val matrix = bannedIdMatrix(user_id, banned_id)
        
        fun move(
            x: Int,
            y: Int,
            combination: MutableSet<String>
        ): MutableSet<MutableSet<String>> {
            val result = mutableSetOf<MutableSet<String>>()
            val copiedCombination = combination.toMutableSet()
            if (combination.contains(matrix[y][x])) {
                return mutableSetOf()
            }
            copiedCombination.add(matrix[y][x])
            
            if (y + 1 >= matrix.size) {
                return mutableSetOf(copiedCombination)
            }
            
            for (nextX in 0 until matrix[y + 1].size) {
                for (row in move(nextX, y + 1, copiedCombination)) {
                    result.add(row)
                }
            }
            return result
        }
        
        val combinations = mutableSetOf<MutableSet<String>>()
        for (startX in 0 until matrix[0].size) {
            for (row in move(startX, 0, mutableSetOf<String>())) {
                if (!combinations.contains(row)) {
                    combinations.add(row)
                }
            }
        }
        
        return combinations.size
    }

    
    // 1. banned_id를 순회하면서 패턴이 일치하는 user_id를 찾고 기록한다.
    fun bannedIdMatrix(
        user_id: Array<String>,
        banned_id: Array<String>,
    ): List<List<String>> {
        return banned_id.map { bid ->
            user_id.filter { uid -> isPatternMatched(uid, bid) }
        }
    }
    
    fun isPatternMatched(user_id: String, banned_id: String): Boolean {
        if (user_id.length != banned_id.length) {
            return false
        }
        for (i in 0 until user_id.length) {
            if (banned_id[i] == '*') {
                continue
            }
            if (user_id[i] != banned_id[i]) {
                return false
            }
        }
        return true
    }
}