import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        
        int la = a.length();
        int lb = b.length();
        
        int[][] dp = new int[la + 1][lb + 1];
        int ans = 0;
        for (int i =1; i < la+1;i++){
            for (int j = 1 ; j < lb + 1 ;j++){
                if (a.charAt(i-1) == b.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1] + 1;
                    if (ans < dp[i][j]){
                        ans = dp[i][j];
                    }
                }else{
                    dp[i][j] = 0;
                }
            }
        }
        System.out.println(ans);
    }
}
