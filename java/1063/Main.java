import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static Location stone;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Location king = new Location(st.nextToken());
        stone = new Location(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        System.out.println(n);
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
        }
    }

}

class Location {
    private int row;
    private int col;

    Location(String s) {
        this.col = s.charAt(0) - 64;
        this.row = Integer.parseInt(String.valueOf(s.charAt(1)));
    }

    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }
}