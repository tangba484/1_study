import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        List<Person> people = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] split = sc.nextLine().split(" ");
            people.add(new Person(split[0], split[1], split[2], split[3]));
        }

        Collections.sort(people, Comparator.comparing((Person p) -> Integer.parseInt(p.year))
                .thenComparing(p -> Integer.parseInt(p.month))
                .thenComparing(p -> Integer.parseInt(p.day)));

        System.out.println(people.get(N-1).getName());
        System.out.println(people.get(0).getName());

    }
}

class Person {
    String name;
    String day;
    String month;
    String year;

    public Person(String name, String day, String month, String year) {
        this.name = name;
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public String getName() {
        return name;
    }
}