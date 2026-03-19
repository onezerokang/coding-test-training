class Solution {
    val dict = listOf('A', 'E', 'I', "O", 'U', ' ')
    
    fun solution(word: String): Int {
        val resultSet = mutableSetOf<String>()
        for (idx in 0..5) {
            resultSet.addAll(dfs(idx, "", mutableSetOf<String>()))
        }
        val dfsResult = resultSet.toList().sorted()
        return dfsResult.indexOf(word)
        
    }
    
    fun dfs(idx: Int, word: String, acc: MutableSet<String>): Set<String> {
        if (dict[idx] == ' ') {
            acc.add(word)
            return acc
        }
        if (word.length == 5) {
            acc.add(word)
            return acc
        }
        for (next in 0..5) {
            acc.addAll(dfs(next, word + dict[idx], acc.toMutableSet()))
        }
        return acc
    }
}