import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int alarm = sc.nextInt() * 60 + sc.nextInt() + 1395;
        
        System.out.println((alarm / 60) % 24 + " " + (alarm % 60));
    }
}

/*
[note]
- 시간 앞당기기 => 앞 당길 시간 만큼을 뺀 하루를 더하면 됨
  예) 45분 앞당기기 => 60 * 24 - 45 = 1395분
      10시 10 분 => 610 + 1395 = 2005분 = 9시 25분

- 24시 표현 => 24로 나눴을 때 나머지를 출력하면 됨
  예) 2005분 => 2005 / 60 % 24 = 8시;
             => 2005 % 60 = 25분;
*/
