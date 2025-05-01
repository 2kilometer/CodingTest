import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i = 1; i <= n; i += 2){
            answer.add(i);
        }
        
        return answer;
    }
}