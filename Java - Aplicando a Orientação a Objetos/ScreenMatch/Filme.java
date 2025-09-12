import java.io.PrintStream;

public class Filme {
    String nome;
    int anoLancamento;
    int duracaoMinutos;
    int totalAvaliacoes;
    double somaAvaliacoes;
    Boolean inclusoPlano;

    // Construtor
    public Filme (String nome, int anoLancamento, int duracaoMinutos, Boolean inclusoPlano) {
        this.nome = nome;
        this.anoLancamento = anoLancamento;
        this.duracaoMinutos = duracaoMinutos;
        this.inclusoPlano = inclusoPlano;
    }

    // Métodos
    public void exibirFichaTecnica() {
        System.out.printf("""
                          ----------- Ficha Técnica -----------
                          Filme: %s
                          Ano de Lançamento: %d
                          Duração em Minutos: %d
                          Média de Avaliações: %.1f
                          Incluso no plano: %s
                          -------------------------------------
                          """, nome, anoLancamento, duracaoMinutos, calcularMedia(), inclusoPlano());
    }

    public void avaliar(double nota) {
        somaAvaliacoes += nota;
        totalAvaliacoes++;
    }

    public double calcularMedia() {
        return Math.round(somaAvaliacoes / totalAvaliacoes * 10.00 ) / 10.00 ;
    }

    public String inclusoPlano() {
        return inclusoPlano ? "Incluso" : "Não Incluso";
    }

}
