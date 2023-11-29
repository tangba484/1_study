import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        List <Integer> l = new ArrayList<>();
        l.add(A);
        l.add(B);
        l.add(C);
        Collections.sort(l);
        System.out.println(l.get(1));
    }
}