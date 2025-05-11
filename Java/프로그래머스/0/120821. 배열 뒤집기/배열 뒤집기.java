import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] num_list) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i = num_list.length - 1; i >= 0; i--){
            answer.add(num_list[i]);
        }
        
        return answer;
    }
}