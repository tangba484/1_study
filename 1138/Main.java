import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    

    public static void main(String[] args) throws IOException {
        BufferedReader  br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        Object[] A = Arrays.stream(s.split(" ")).map(Integer::valueOf).toArray();
        int[] ans = new int[n];

        for (int i=0;i<n;i++) {
            int C = (int) A[i];
            for (int j=0;j<n;j++){
                if(C==0 && ans[j]==0) {
                    ans[j]=i+1;
                    break;
                }else if(ans[j]==0) {
                    C--;
                }
            }
        }

        for (int i :ans) {
            System.out.print(i+" ");
        }

    }
}