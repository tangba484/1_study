import java.io.*;
import java.util.*;

public class Main {
    static int ans = 1;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            List<Integer> numbers = new ArrayList<>();
            String s = br.readLine();
            String[] split = s.split("");
            for (String x : split) {
                numbers.add(Integer.valueOf(x));
            }
            graph.add(numbers);
        }

        for (int l = 1; l <= Math.min(N, M); l++) {
            check(l, graph);
        }
        System.out.println(ans);
    }

    private static void check(int l, List<List<Integer>> graph) {
        for (int i = 0; i < N - l + 1; i++) {
            for (int j = 0; j < M - l + 1; j++) {
                if (graph.get(i).get(j) == graph.get(i).get(j + l - 1) && graph.get(i).get(j) == graph.get(i + l - 1).get(j) && graph.get(i).get(j) == graph.get(i + l - 1).get(j + l - 1)) {
                    if (l * l > ans) {
                        ans = l * l;
                    }
                }
            }
        }
    }
}