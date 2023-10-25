import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] li = br.readLine().split(" ");
        int N = Integer.parseInt(li[0]);
        int K = Integer.parseInt(li[1]);

        int[] P = new int[N+1];
        for (int i=0 ; i < N+1 ; i ++){
            P[i] = i;
        }
        int cnt = 0;
        for (int i = 2; i < N+1 ; i ++){
            if (P[i] == 0) continue;

            for (int j =i; j<N+1 ; j+=i){
                if (P[j] !=0){
                    P[j] = 0;
                    cnt += 1;
                }
                if (cnt == K){
                    System.out.println(j);
                    return ;
                }
            }   
        }
    }
}