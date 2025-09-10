import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ContaBancaria conta = new ContaBancaria();
        Cliente cliente = new Cliente();
        MenuUtils menuUtils = new MenuUtils();

        // Populando os dados
        // conta.setNomeCliente("Jacqueline Oliveira");
        // conta.setTipoConta("Corrente");
        // conta.setSaldoConta(2500.00);

        try {
            menuUtils.montarInterface(conta, scanner);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}