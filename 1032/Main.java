import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        String[] a = new String[n]; 
        for (int i = 0; i < n; i++) {
            a[i] = br.readLine(); 
        }
        int len = a[0].length(); 
        for (int i = 0; i < len; i++) {
            boolean b = true;
            char c = a[0].charAt(i);
            for (int j = 1; j < n; j++) {
                if (c != a[j].charAt(i)) b = false;
            }
            if (b) {
                sb.append(c);
            } else {
                sb.append("?");
            }
        }
        System.out.print(sb);
    }
}