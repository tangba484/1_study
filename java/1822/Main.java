import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer st ;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] l = br.readLine().split(" ");
        int na = Integer.parseInt(l[0]);
        int nb = Integer.parseInt(l[1]);
        HashSet<Integer> A = new HashSet<>();
        HashSet<Integer> B = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<na;i++){
            A.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<nb;i++){
            B.add(Integer.parseInt(st.nextToken()));
        }
        A.removeAll(B);
        System.out.println(A.size());
        A.stream().sorted()
            .forEach(a -> System.out.print(a+" "));
    }
}
