import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int A = Integer.parseInt(br.readLine());
        String B = br.readLine();
        char[] b = B.toCharArray();
        
        System.out.println(A * (b[2]-'0'));
        System.out.println(A * (b[1]-'0'));
        System.out.println(A * (b[0]-'0'));
        System.out.println(A * Integer.parseInt(B));
    }
}

/*
[note]
- 문자형 숫자를 배열로 바꾸는 방법
    -> char[] b = B.toCharArray();

- 문자형 숫자를 계산하는 방법
    -> - '0'
    -> '0'는 ASCII코드로 48이기에 이를 빼면 알고자 하는 숫자가 나오게 된다
*/