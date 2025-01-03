import java.util.Scanner;

public class Main {
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] K = new int[201];
		for(int i=0; i<N ;i++) 
			K[sc.nextInt()+100]++;
		System.out.println(K[sc.nextInt()+100]);
	}
}

/*
[Notes]
- 고정된 길이의 배열을 만든 후, 수가 나올 때 각 자리에 카운트를 추가하는 방식
  -- K에 나올 수 있는 정수의 수를 담고, 0번째에 음수의 수가 담기게 생성 
    (-100 ~ 100 : 0 -> -100, 100 -> 0, 201 -> 100)
*/
