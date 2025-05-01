import java.util.HashSet;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] array) {
        HashSet<Integer> unique = new HashSet<>();
        int answer = 0;
        int maxCnt = 0;
        
        for (int num : array){
            unique.add(num);
        }
        
        for (Integer uniqueNum : unique){
            long cnt = Arrays.stream(array)
                            .filter(num -> num == uniqueNum)
                            .count();
            if (maxCnt == cnt){
                answer = -1;
            } else if (maxCnt < cnt){
                answer = uniqueNum;
                maxCnt = (int)cnt;
            }
        }
        return answer;
    }
}