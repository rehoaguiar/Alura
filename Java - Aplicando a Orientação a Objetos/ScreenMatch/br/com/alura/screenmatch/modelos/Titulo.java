package br.com.alura.screenmatch.modelos;

public class Titulo {
    private String nome;
    private int anoLancamento;
    private int duracaoMinutos;
    private int totalAvaliacoes;
    private double somaAvaliacoes;
    private Boolean inclusoPlano;

    // Construtor para filme
    public Titulo (String nome, int anoLancamento, int duracaoMinutos, Boolean inclusoPlano) {
        this.nome = nome;
        this.anoLancamento = anoLancamento;
        this.duracaoMinutos = duracaoMinutos;
        this.inclusoPlano = inclusoPlano;
    }

    // Construtor para série
    public Titulo (String nome, int anoLancamento, Boolean inclusoPlano) {
        this.nome = nome;
        this.anoLancamento = anoLancamento;
        this.duracaoMinutos = 0;
        this.inclusoPlano = inclusoPlano;
    }

    // Getters e Setters

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getAnoLancamento() {
        return anoLancamento;
    }

    public void setAnoLancamento(int anoLancamento) {
        this.anoLancamento = anoLancamento;
    }

    public int getDuracaoMinutos() {
        return duracaoMinutos;
    }

    public void setDuracaoMinutos(int duracaoMinutos) {
        this.duracaoMinutos = duracaoMinutos;
    }

    public Boolean getInclusoPlano() {
        return inclusoPlano;
    }

    public void setInclusoPlano(Boolean inclusoPlano) {
        this.inclusoPlano = inclusoPlano;
    }

    public int getTotalAvaliacoes() {
        return totalAvaliacoes;
    }

    public double getSomaAvaliacoes() {
        return somaAvaliacoes;
    }

    // Métodos
    public void exibirFichaTecnica() {
        System.out.printf("""
                          ----------- Ficha Técnica -----------
                          Título: %s
                          Ano de Lançamento: %d
                          Duração em Minutos: %d
                          Média de Avaliações: %.1f
                          Incluso no plano: %s
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
