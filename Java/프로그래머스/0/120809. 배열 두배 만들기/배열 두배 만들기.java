class Solution {
    public int[] solution(int[] numbers) {
        int len = numbers.length;
        int[] result = new int[len];
        
        for(int i = 0; i < len; i++){
            result[i] = numbers[i] * 2;
        }
        return result;
    }
}