class Solution {
    public int solution(int n) {
        int answer = (n / 6 == 0)? 1: n/6;
        
        while ((answer * 6) % n != 0){
            answer++;
        }
        
        return answer;
    }
}