import java.util.Scanner;

public class ContaBancaria extends Cliente {
    int opcao;
    protected String titular;
    protected double saldo;

    // Getters
    public int getOpcao() {
        return opcao;
    }

    // Setters
    public void setOpcao(int opcao) {
        this.opcao = opcao;
    }

    // Métodos
    public void menuOpcoes(){
        System.out.println("Escolha uma Opção");
    }

    public void consultarSaldo(){
        System.out.printf("Saldo atual: R$ %.2f", saldoConta);
    }

    public void receberValor(Scanner scanner){
        double valorRecebido;
        System.out.print("Informe o valor a receber: ");
        valorRecebido = scanner.nextDouble();
        saldoConta += valorRecebido;
        System.out.printf("Saldo atualizado R$ %.2f", saldoConta);
        scanner.nextLine();
    }

    public void transferirValor(Scanner scanner){
        double valorTransferido;
        System.out.print("Informe o valor a ser transferido: ");
        valorTransferido = scanner.nextDouble();

        if (valorTransferido <= saldoConta) {
            saldoConta -= valorTransferido;
            System.out.printf("Saldo atualizado R$ %.2f", saldoConta);
        } else {
            System.out.println("O valor transferido não pode ser maior que o saldo da conta");
        }

        scanner.nextLine();
    }

    public void cadastrarCliente(Scanner scanner) {
        scanner.nextLine();
        definirNome(scanner);
        definirTipoConta(scanner);
        definirSaldoConta(scanner);
        exibirDadosIniciais();
    }
}
