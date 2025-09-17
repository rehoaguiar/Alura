package br.com.alura.screenmatch.modelos;

public class Filme extends Titulo {
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
                          ----------- Ficha Técnica -----------
                          Filme: %s
                          Diretor: %s
                          Ano de Lançamento: %d
                          Duração em Minutos: %d
                          Média de Avaliações: %.1f
                          Incluso no plano: %s
                          -------------------------------------
                          """, getNome(), diretor, getDuracaoMinutos(), calcularMedia(), inclusoPlano());
    }

}
