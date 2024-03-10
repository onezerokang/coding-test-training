import java.util.*;

class Solution {
    public int solution(String skill, String[] skillTree) {
        return (int) Arrays.stream(skillTree)
            .map(s -> s.replaceAll("[^" + skill + "]", ""))
            .filter(skill::startsWith)
            .count();
    }
//     public int solution(String skill, String[] skill_trees) {
//         int result = 0;
//         for (String skill_tree: skill_trees) {
//             String skills = filter(skill, skill_tree);
//             if (compare(skill, skills)) {
//                 result++;
//             }
//         }
        
        
//         return result;
//     }
    
//     private String filter(String skill, String skill_tree) {
//         StringBuilder builder = new StringBuilder();
//         for (char userSkill: skill_tree.toCharArray()) {
//             if (skill.indexOf(userSkill) != -1) {
//                 builder.append(userSkill);
//             }
//         }
        
//         return builder.toString();
//     }
    
//     private boolean compare(String skills, String userSkills) {
//         return skills.startsWith(userSkills);
//     }
}