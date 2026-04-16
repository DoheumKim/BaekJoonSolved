import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        MyDequeAppTest app = new MyDequeAppTest();
        app.run();
    }
}
class MyDequeAppTest {
    private final MyDequeTest<Integer> dq = new MyDequeTest<>();
    private final Scanner sc = new Scanner(System.in);
    private final StringBuilder output = new StringBuilder();

    public void run() {
        int n = Integer.parseInt(sc.nextLine());

        while (n-- > 0) {
            String cmd = sc.nextLine();
            if (cmd.startsWith("push_front")) {
                int val = Integer.parseInt(cmd.split(" ")[1]);
                dq.push_front(val);
            } else if (cmd.startsWith("push_back")) {
                int val = Integer.parseInt(cmd.split(" ")[1]);
                dq.push_back(val);
            } else {
                switch (cmd) {
                    case "pop_front": {
                        append(dq.pop_front());
                        break;
                    }
                    case "pop_back": {
                        append(dq.pop_back());
                        break;
                    }
                    case "size": {
                        output.append(dq.size()).append("\n");
                        break;
                    }
                    case "empty": {
                        output.append(dq.isEmpty() ? 1 : 0).append("\n");
                        break;
                    }
                    case "front": {
                        append(dq.front());
                        break;
                    }
                    case "back": {
                        append(dq.back());
                        break;
                    }
                }

            }
        } if (output.length() > 0 && output.charAt(output.length() - 1) == '\n') {
            output.setLength(output.length() - 1);
        }
        System.out.print(output);
    }

    private void append(Integer x) {
        if (x == null) output.append("-1\n");
        else output.append(x).append("\n");
    }
}
class MyDequeTest<E> {
    private NodeTest<E> front;
    private NodeTest<E> rear;
    private int size = 0;

    public void push_front(E x) {
        NodeTest<E> newNode = new NodeTest<>(x);
        if (isEmpty()) front = rear = newNode;
        else {
            newNode.next = front;
            front.prev = newNode;
            front = newNode;
        }
        size++;
    }

    public void push_back(E x) {
        NodeTest<E> newNode = new NodeTest<>(x);
        if (isEmpty()) front = rear = newNode;
        else {
            rear.next = newNode;
            newNode.prev = rear;
            rear = newNode;
        }
        size++;
    }

    public E pop_front() {
        if (isEmpty()) return null;
        E val = front.data;
        front = front.next;
        if (front != null) front.prev = null;
        else rear = null;
        size--;
        return val;
    }

    public E pop_back() {
        if (isEmpty()) return null;
        E val = rear.data;
        rear = rear.prev;
        if (rear != null) rear.next = null;
        else front = null;
        size--;
        return val;
    }

    public int size() { return size; }
    public boolean isEmpty() { return size == 0; }
    public E front() { return isEmpty() ? null : front.data; }
    public E back() { return isEmpty() ? null : rear.data; }
}
class NodeTest<E> {
    E data;
    NodeTest<E> prev, next;
    NodeTest(E data) {
        this.data = data;
    }
}