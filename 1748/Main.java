import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long cnt =0;
        for (int i = 1; i <= n; i *= 10) {
            cnt += (n - i + 1);
        }
        System.out.println(cnt);
    }
}
