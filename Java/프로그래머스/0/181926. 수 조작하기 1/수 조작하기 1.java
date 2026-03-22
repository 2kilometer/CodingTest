import java.util.Map;
class Solution {
    public int solution(int n, String control) {
        for (char letter : control.toCharArray()) {
            switch (letter) {
                case 'w': n += 1; break;
                case 's': n -= 1; break;
                case 'd': n += 10; break;
                case 'a': n -= 10; break;
            }
        }
        
        return n;
    }
}