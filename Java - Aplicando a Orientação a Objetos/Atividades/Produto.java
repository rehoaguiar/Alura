import javax.swing.*;

public class Produto {
   private String nome;
   private Double preco;

   // Getters e Setters

    public Double getPreco() {
        return preco;
    }

    public void setPreco(Double preco) {
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    // Métodos
    public void aplicarDesconto(double percentual) {
        double valorDesconto = getPreco() * (percentual / 100.00);

        if (getPreco() < valorDesconto) {
            throw new IllegalArgumentException("Não é permitido que desconto seja maior que o valor do produto!");
        }

        setPreco(getPreco() - valorDesconto);
    }

    // Main
    public static void main(String[] args) {
        Produto produto = new Produto();

        produto.setNome("Adventure Awaits - Sims 4 Expansion Pack");
        produto.setPreco(180.00);

        System.out.printf("\nNome Produto: %s", produto.getNome());
        System.out.printf("\nPreço do Produto: %.2f\n", produto.getPreco());

        produto.aplicarDesconto(30);

        System.out.printf("\nNome Produto: %s", produto.getNome());
        System.out.printf("\nPreço do Produto com Desconto: %.2f\n", produto.getPreco());
    }
}
