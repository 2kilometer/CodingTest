import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int num_len = num_list.length;
        int[] answer = Arrays.copyOf(num_list, num_len + 1);
        
        if (num_list[num_len - 1] > num_list[num_len - 2]) {
            answer[num_len] = num_list[num_len - 1] - num_list[num_len - 2];
        } else {
            answer[num_len] = num_list[num_len-1] * 2;
        }
        
        
        return answer;
    }
}