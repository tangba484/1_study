import java.util.*;
import java.io.*;
public class boj_9934 {
    static int k;
    static int[] l ;
    static List<ArrayList<Integer>> ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        l = new int[(int)Math.pow(2,k)-1];
        for (int i=0;i<l.length;i++){
            l[i] = Integer.parseInt(st.nextToken());
        }
        ans = new ArrayList<>();
        for (int i=0;i<k;i++){
            ans.add(new ArrayList<Integer>());
        }
        r(0,l.length-1,0);
        for (ArrayList<Integer> i: ans){
            for (Integer a : i){
                System.out.print(a + " ");
            }
            System.out.println();
        }
    }

    static void r(int start,int end,int d){
        if (d == k) return;
        Integer mid = (start+end)/2;
        ans.get(d).add(l[mid]);
        r(start,mid-1,d+1);
        r(mid + 1,end,d + 1);

    }
}
