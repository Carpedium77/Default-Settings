
import java.io.*;
import java.net.*;

public class FactorialClient {
    public static void main(String[] args) {
        try {
            // Connect to server
            Socket socket = new Socket("localhost", 5000);
            System.out.println("Connected to server.");

            // Input stream - receive data from server
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));

            // Output stream - send data to server
            PrintWriter out = new PrintWriter(
                    socket.getOutputStream(), true);

            // Read number from user
            BufferedReader keyboard = new BufferedReader(
                    new InputStreamReader(System.in));

            System.out.print("Enter a number: ");
            int number = Integer.parseInt(keyboard.readLine());

            // Send number to server
            out.println(number);

            // Receive factorial
            String result = in.readLine();

            // Display result
            System.out.println("Factorial received from server: " + result);

            // Close connection
            socket.close();
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
