class Solution {
    public String solution(String code) {
        int mode = 0;
        StringBuilder ret = new StringBuilder();
        
        for (int i = 0; i < code.length(); i++){
            if (code.charAt(i) == '1') {
                mode = mode == 0 ? 1 : 0;
            }
            else {
                if ((mode == 0) && (i % 2 == 0))
                    ret.append(code.charAt(i));
                else if ((mode == 1) && (i % 2 != 0))
                    ret.append(code.charAt(i));
            }
        }
        
        return ret.length() == 0 ? "EMPTY" : ret.toString();
    }
}