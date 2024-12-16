import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int now = h * 60 + m;
        int alarm = now - 45;
        
        if (alarm >= 0) {
            System.out.println((alarm / 60) + " " + (alarm % 60));
        } else {
            System.out.println(23 + " " + (60 + alarm));
        }
    }
}