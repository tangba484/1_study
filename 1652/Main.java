
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<String> graph = new ArrayList<>();
        int ans = 0;
        for (int i=0;i<N;i++) {
            String s = br.readLine();
            graph.add(s);
        }

        for (String s : graph) {
            String[] split = s.split("X");
            for (String a :split) {
                if (a.contains("..")) {
                    ans += 1;
                }
            }
        }
        System.out.print(ans +" ");
        List<String> graph1 = new ArrayList<>();
        for (int i=0;i<N;i++) {
            String x ="";
            for (int j =0;j<N;j++) {
                x += graph.get(j).charAt(i);
            }
            graph1.add(x);
        }
        ans = 0;
        for (String s : graph1) {
            String[] split = s.split("X");
            for (String a :split) {
                if (a.contains("..")) {
                    ans += 1;
                }
            }
        }
        System.out.println(ans);
    }
}
