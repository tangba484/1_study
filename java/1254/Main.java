import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int ans = s.length();
        for (int i = 0; i < s.length(); i++) {
            if (isP(s.substring(i))) break;

            ans += 1;
        }

        System.out.println(ans);
    }

    static boolean isP(String s) {
        StringBuilder sb = new StringBuilder();
        sb.append(s);
        String reverseString = sb.reverse().toString();
        return s.equals(reverseString);
    }
}
