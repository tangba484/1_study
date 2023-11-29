import java.io.*;
import java.util.*;

public class Main {
    static boolean[][] visited;
    static int n;
    static int m;
    static char[][] graph;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new char[n][m];
        for (int i=0;i<n;i++) {
            graph[i] = br.readLine().toCharArray();
        }
        visited = new boolean[n][m];
        int ans=0;
        for (int i=0;i<n;i++) {
            for (int j=0;j<m;j++) {
                if (!visited[i][j]) {
                    dfs(i,j);
                    ans += 1;
                }
            }
        }
        System.out.println(ans);
    }
    private static void dfs(int x, int y) {
        Stack<int[]> stack = new Stack<>();
        visited[x][y] = true;
        stack.push(new int[]{x, y});
        if (graph[x][y] == '-') {
            while(!stack.isEmpty()){
                int[] pop = stack.pop();
                int X = pop[0];
                int Y = pop[1];
                if (Y+1<m && graph[X][Y+1] =='-' && !visited[X][Y+1]) {
                    stack.push(new int[]{X,Y+1});
                    visited[X][Y+1] = true;
                }
            }
        }else if (graph[x][y] == '|'){
            while(!stack.isEmpty()){
                int[] pop = stack.pop();
                int X = pop[0];
                int Y = pop[1];
                if (X+1<n && graph[X+1][Y] =='|' && !visited[X+1][Y]) {
                    stack.push(new int[]{X+1,Y});
                    visited[X+1][Y] = true;
                }
            }
        }
    }
}