import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class boj_10974 {
    static int n;
    static int arr[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        back(0,arr);
        System.out.println(sb.toString());
    }
    static StringBuilder sb = new StringBuilder();
    static void back(int depth ,int[] arr){
        if (depth == n) {
            for (int x : arr) {
                sb.append(x+" ");
            }
            sb.append("\n");
            return;
        }
        for (int i=0;i<n;i++) {
            int flag=0;
            for(int j=0;j<n;j++){
                if (arr[j] == i+1) {
                    flag = 1;
                }
            }
            if (flag == 0) {
                arr[depth] = i+1;
                back(depth + 1 ,arr);
                arr[depth] = 0;
            }

        }


    }
}