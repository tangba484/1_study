import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] graph = new int[n][n];

        for (int i =0 ; i < n ;i++) {
            String s = br.readLine();
            char[] array = s.toCharArray();
            for (int j=0;j<n;j++) {
                graph[i][j] = (array[j] == 'Y') ? 1 : 9999;
            }
        }

        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++) {
                for (int k=0;k<n;k++){
                    if (i == j || j == k || k == i) {
                        continue;
                    } else if (graph[i][j] > graph[i][k] + graph[k][j]){
                        graph[i][j] = graph[i][k] + graph[k][j];
                    }
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int s = 0;
            for (int j =0;j<n;j++) {
                if (i==j) {continue;} else if (graph[i][j] <=2) { s++;}}
            ans = Math.max(s,ans);
        }
        System.out.println(ans);
    }
}