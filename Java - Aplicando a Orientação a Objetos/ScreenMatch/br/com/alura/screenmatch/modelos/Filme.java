package br.com.alura.screenmatch.modelos;

import br.com.alura.screenmatch.calculos.Classificavel;

public class Filme extends Titulo implements Classificavel {
    String diretor;

    // Construtor
    public Filme (String nome, String diretor, int anoLancamento, int duracaoMinutos, Boolean inclusoPlano) {
       super(nome, anoLancamento, duracaoMinutos, inclusoPlano);
       this.diretor = diretor;
    }

    public String getDiretor() {
        return diretor;
    }

    public void setDiretor(String diretor) {
        this.diretor = diretor;
    }

    @Override
    public void exibirFichaTecnica() {
        System.out.printf("""
                          ----------- Ficha Técnica de Filme -----------
                          Filme: %s
                          Diretor: %s
                          Ano de Lançamento: %d
                          Duração em Minutos: %d
                          Média de Avaliações: %.1f
                          Incluso no plano: %s
                          ----------------------------------------------%n
                          """, getNome(), diretor, getAnoLancamento(), getDuracaoMinutos(), calcularMedia(), inclusoPlano());
    }

    @Override
    public int getClassificacao() {
        return (int) calcularMedia() / 2;
    }
}
