import java.util.*;
import java.io.*;

public class Main {
	public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        List<String> values = Arrays.asList(br.readLine().split(" "));
        String v = br.readLine();
		
		bw.write(Collections.frequency(values, v) + "");
		bw.close();
	}
}