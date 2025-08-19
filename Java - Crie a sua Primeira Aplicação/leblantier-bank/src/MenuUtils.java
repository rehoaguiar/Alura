import java.util.Scanner;

public class MenuUtils {
    // Declarando variáveis
    int opcao;

    // Getters
    public int getOpcao() {
        return opcao;
    }

    // Setters
    public void setOpcao(int opcao){
        this.opcao = opcao;
    }

    // Métodos
    public static void mostrarBanner() {
        System.out.print("""
                \n\n
                ██╗░░░░░███████╗██████╗░██╗░░░░░░█████╗░███╗░░██╗████████╗██╗███████╗██████╗░
                ██║░░░░░██╔════╝██╔══██╗██║░░░░░██╔══██╗████╗░██║╚══██╔══╝██║██╔════╝██╔══██╗
                ██║░░░░░█████╗░░██████╦╝██║░░░░░███████║██╔██╗██║░░░██║░░░██║█████╗░░██████╔╝
                ██║░░░░░██╔══╝░░██╔══██╗██║░░░░░██╔══██║██║╚████║░░░██║░░░██║██╔══╝░░██╔══██╗
                ███████╗███████╗██████╦╝███████╗██║░░██║██║░╚███║░░░██║░░░██║███████╗██║░░██║
                ╚══════╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝╚══════╝╚═╝░░╚═╝
                
                ██████╗░░█████╗░███╗░░██╗██╗░░██╗
                ██╔══██╗██╔══██╗████╗░██║██║░██╔╝
                ██████╦╝███████║██╔██╗██║█████═╝░
                ██╔══██╗██╔══██║██║╚████║██╔═██╗░
                ██████╦╝██║░░██║██║░╚███║██║░╚██╗
                ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
                """);
    }

    public static void mostrarMenu() {
        System.out.println(""" 
                \n\n--------- Operações ---------
                0 - Cadastrar Titular
                1 - Consultar Saldo
                2 - Receber Valor
                3 - Transferir Valor
                4 - Sair
                -----------------------------
                """);
    }

    public static void exibirOpcaoInvalida() {
        System.out.println("Opção Inválida! Tente Novamente");
    }

    public int escolherOpcao(int opcao, Scanner scanner) {
        System.out.print("Digite a opção desejada: ");
        this.opcao = scanner.nextInt();
        return opcao;
    }

    public void verificarOpcao(Scanner scanner, int opcao, ContaBancaria conta) {
        switch (opcao) {
            case 0:
                System.out.println("\n----- Cadastrar Usuário -----");
                conta.cadastrarCliente(scanner);
                break;

            case 1:
                System.out.println("\n------ Consultar Saldo ------");
                conta.consultarSaldo();
                break;

            case 2:
                System.out.println("\n------- Receber Valor -------");
                conta.receberValor(scanner);
                break;

            case 3:
                System.out.println("\n------ Transferir Valor -----");
                conta.transferirValor(scanner);
                break;

            case 4:
                System.out.println("\n----------- Saindo -----------");
                break;

            default:
                System.out.println("\nOpção Inválida! Escolha um número que exista no menu!");
        }
    }

    public void montarInterface(ContaBancaria conta, Scanner scanner) {
        while (opcao != 4) {
            mostrarBanner();
            mostrarMenu();
            escolherOpcao(opcao, scanner);
            verificarOpcao(scanner, opcao, conta);
        }
    }
}