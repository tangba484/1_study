import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        String info = sc.nextLine();
        int[][] graph = new int[200][200];

        int minX = 100;
        int maxX = 100;
        int minY = 100;
        int maxY = 100;
        int x = 100;
        int y = 100;

        int[] dX = {1, 0, -1, 0};
        int[] dY = {0, -1, 0, 1};

        int idx = 0;
        graph[x][y] = 1;

        for (int i = 0; i < info.length(); i++) {
            char c = info.charAt(i);
            if (c == 'R') {
                idx = (idx + 1) % 4;
            } else if (c == 'L') {
                idx -= 1;
                if (idx < 0) idx = 3;
            } else if (c == 'F') {
                x = dX[idx] + x;
                y = dY[idx] + y;
                graph[x][y] = 1;
                maxX = Math.max(maxX, x);
                minX = Math.min(minX, x);

                maxY = Math.max(maxY, y);
                minY = Math.min(minY, y);
            }
        }
        for (int i = minX; i <= maxX; i++) {
            for (int j = minY; j <= maxY; j++) {
                if (graph[i][j] == 1) {
                    System.out.print('.');
                } else {
                    System.out.print('#');
                }
            }
            System.out.println();
        }
    }
}
