
import java.util.Scanner;

public class EjercicioTres {

    Scanner entrada = new Scanner(System.in);
    
    String ingresaNombre = entrada.nextLine();

    public static void main(String[] args) {
        System.out.println("Ingresa tu nombre: ");
        EjercicioTres ejercicio_tres = new EjercicioTres();
        System.out.println("Bienvenido " + ejercicio_tres.ingresaNombre);
    }
}
