import java.util.Scanner;

public class Cliente {
    String nomeCliente;
    String tipoConta;
    double saldoConta;

    // Getters
    public String getNomeCliente() {
        return nomeCliente;
    }

    public String getTipoConta() {
        return tipoConta;
    }

    public Double getSaldoConta() {
        return saldoConta;
    }

    // Setters
    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public void setTipoConta(String tipoConta) {
        this.tipoConta = tipoConta;
    }

    public void setSaldoConta(Double saldoConta) {
        this.saldoConta = saldoConta;
    }

    // Métodos
    public void exibirDadosIniciais() {
        System.out.println("\n------ Dados Inicias ------");
        System.out.printf("Nome do Titular: %s", getNomeCliente());
        System.out.printf("\nTipo Conta: %s", getTipoConta());
        System.out.printf("\nSaldo da Conta: %.2f", getSaldoConta());
    }

    public void definirNome(Scanner scanner) {
        System.out.print("Nome Completo: ");
        this.nomeCliente = scanner.nextLine();
    }

    public void definirTipoConta(Scanner scanner) {
        System.out.print("Tipo de Conta: ");
        this.tipoConta = scanner.nextLine();
    }

    public void definirSaldoConta(Scanner scanner) {
        System.out.print("Saldo da Conta: ");
        this.saldoConta = scanner.nextDouble();
    }
}