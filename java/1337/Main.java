import java.util.*;
import java.io.*;
public class Main {
    static int n;
    static ArrayList<Integer> A;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        A = new ArrayList<>();
        for (int i=0;i<n;i++) {
            A.add(Integer.valueOf(br.readLine()));
        }
        Collections.sort(A);
        int ans = 4;
        int start=0;
        int end = 0;
        while(true){
            if(end >= n){
                break;
            }
            if(A.get(end) - A.get(start) < 5){
                end += 1;
                ans = Math.min(ans, 5 - (end - start));
            }else{
                start++;
            }
        }
        System.out.println(ans);

    }
}
