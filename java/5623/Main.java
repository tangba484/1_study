import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] li = new int[N][N];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                li[i][j] = sc.nextInt();
            }
        }
        
        if (N == 2) {
            System.out.println("1 1");
        } else {
            int[] res = new int[N];
            res[0] = (li[0][1] + li[0][2] - li[1][2]) / 2;
            
            for (int i = 1; i < N; i++) {
                res[i] = li[0][i] - res[0];
            }
            
            for (int i = 0; i < N; i++) {
                System.out.print(res[i] + " ");
            }
            System.out.println();
        }
    }
}
