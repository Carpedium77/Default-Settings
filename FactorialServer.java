import java.io.*;
import java.net.*;

public class FactorialServer{
    public static void main(String args[]){
        try{
            ServerSocket serverSocket = new ServerSocket(5000);

            System.out.println("Server Started ...");
            System.out.println("Server waiting for Client connection...");

            Socket socket = serverSocket.accept();
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter( socket.getOutputStream() , true);

            int number = Integer.parseInt(in.readLine());

            System.out.println("Recieved Number :" + number);

            long fact = 1;
            for(int i=1;i<=number;i++){
                fact = fact * i;
            }
            out.println(fact);
            System.out.println("Factorial sent to client!");

            socket.close();
            serverSocket.close();
            
        }
        catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}