class Solution {
    public double solution(int[] numbers) {
        int sumNum = 0;
        double modNum = numbers.length;
        
        for (int num : numbers){
            sumNum += num;
        }
        
        return sumNum/modNum;
    }
}