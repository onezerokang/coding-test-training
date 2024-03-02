import java.util.*;

class Solution {
    private static class Student {
        public Double score;
        public int num;
        
        public Student(Double score, int num) {  
            this.score = score;
            this.num = num;
        }
        
        public String toString() {
            return String.format(
                "Student = {score: %s, num: %s}", score, num
            );
        }
    }
    
    public int[] solution(int[][] score) {
        List<Student> students = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            students.add(
                new Student(((double)score[i][0] + (double)score[i][1]) / 2, i)
            );
        }
        
        Collections.sort(students, (Student s1, Student s2) -> s2.score.compareTo(s1.score));
        
        int[] result = new int[score.length];
        double lastScore = -1.0; // 마지막 점수
        int lastRank = 0; // 마지막 등수
        int acc = 0; // 공통 등수
        for (Student student: students) {
            System.out.println(student);
            if (lastScore == student.score) {
                result[student.num] = lastRank;
                acc++;
            } else {
                lastRank += acc + 1;
                acc = 0;
                lastScore = student.score;
                result[student.num] = lastRank;
            }
        }
        
        return result;
    }
}