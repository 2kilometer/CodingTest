import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        
        if ((90 <= a) && (a <= 100)) {
            System.out.print("A");
        } else if ((80 <= a) && (a <= 89)) {
            System.out.print("B");
        } else if ((70 <= a) && (a <= 79)) {
            System.out.print("C");
        } else if ((60 <= a) && (a <= 69)) {
            System.out.print("D");
        } else {
            System.out.print("F");
        }
    }
}