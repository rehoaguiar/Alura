public class ContaBancaria {
    private int numeroConta;
    private double saldo;
    public String titular;

    // Getters e Setters

    public int getNumeroConta() {
        return numeroConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setNumeroConta(int numeroConta) {
        this.numeroConta = numeroConta;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    // Main
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria();

        conta.setNumeroConta(28);
        conta.setSaldo(1000.00);
        conta.titular = "Reh";

        System.out.printf("\nNumero da Conta: %d", conta.getNumeroConta());
        System.out.printf("\nSaldo: %.2f", conta.getSaldo());
        System.out.printf("\nTitular: %s", conta.titular);

        conta.setSaldo(1000000);
        System.out.printf("\nNovo Saldo: %.2f", conta.getSaldo());
    }
}
