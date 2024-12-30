import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Student> students= new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        new InputMenu(scanner, students);
        scanner.close();

    }
}