import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        List<Integer> ans = new ArrayList<>(Collections.nCopies(10, 0));

        for (int i = 0; i < word.length(); i++) {
            int num = Character.getNumericValue(word.charAt(i));

            if (num == 6 || num == 9) {
                if (ans.get(6) <= ans.get(9)) {
                    ans.set(6, ans.get(6) + 1);
                } else {
                    ans.set(9, ans.get(9) + 1);
                }
            } else {
                ans.set(num, ans.get(num) + 1);
            }
        }

        int maxCount = Collections.max(ans);
        System.out.println(maxCount);
    }
}