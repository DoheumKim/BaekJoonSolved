import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        sc.close();

        int a2 = Integer.parseInt(a);
        int b2 = Integer.parseInt(b);

        System.out.printf("%d", a2 - b2);
    }
}