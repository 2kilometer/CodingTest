import java.util.*;
import java.io.*;

public class Main {
	public static void main (String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(bf.readLine());
        
        for (int i = 0; i < t; i++){
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            bw.write(String.format("Case #%d: %d + %d = %d", i+1, a, b, a+b) + "\n");
        }
        
        bw.close();
    }
}