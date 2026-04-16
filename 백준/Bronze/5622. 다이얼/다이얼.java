import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'A' && c <= 'C') sum += 3;
            else if (c <= 'F') sum += 4;
            else if (c <= 'I') sum += 5;
            else if (c <= 'L') sum += 6;
            else if (c <= 'O') sum += 7;
            else if (c <= 'S') sum += 8;
            else if (c <= 'V') sum += 9;
            else sum += 10; // W,X,Y,Z
        }
        System.out.println(sum);
    }
}