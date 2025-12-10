package 문자열;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B5622 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(new BufferedInputStream(System.in)));
        String input = br.readLine();
        int t, sum = 0, s;
        for (int i = 0; i < input.length(); i++) {
            t = (int) input.charAt(i) - 65;
            if (t >= 22) { // W, X, Y, Z
                s = 7;
            } else if (t >= 19) { // S
                s = 6;
            } else if (t >= 15) { // P, Q, R
                s = 5;
            } else {
                s = t / 3;
            }
            sum += s + 3;
        }
        System.out.println(sum);
    }
}
