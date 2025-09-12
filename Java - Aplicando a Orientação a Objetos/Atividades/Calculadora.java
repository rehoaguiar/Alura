public class Calculadora {
    public static double dobrarNumero(double numero) {
        return numero * 2;
    }

    public static void main(String[] args) {
        double resultado = Calculadora.dobrarNumero(22);
        System.out.println(resultado);
    }
}
