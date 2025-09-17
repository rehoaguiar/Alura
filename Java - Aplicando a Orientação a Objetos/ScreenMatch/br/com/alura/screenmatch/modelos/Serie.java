package br.com.alura.screenmatch.modelos;

public class Serie extends Titulo {
    private int temporadas;
    private boolean ativo;
    private int episodiosPorTemporada;
    private int minutosPorEpisodios;

    // Construtor
    public Serie (String nome, int anoLancamento, int temporadas, int episodiosPorTemporada, int minutosPorEpisodios, Boolean ativo, Boolean inclusoPlano) {
        super(nome, anoLancamento, inclusoPlano);
        this.temporadas = temporadas;
        this.episodiosPorTemporada = episodiosPorTemporada;
        this.minutosPorEpisodios = minutosPorEpisodios;
        this.ativo = ativo;
        this.setDuracaoMinutos(getDuracaoMinutos());
    }

    // Getters e Setters
    public int getTemporadas() {
        return temporadas;
    }

    public void setTemporadas(int temporadas) {
        this.temporadas = temporadas;
    }

    public boolean isAtivo() {
        return ativo;
    }

    public void setAtivo(boolean ativo) {
        this.ativo = ativo;
    }

    public int getEpisodiosPorTemporada() {
        return episodiosPorTemporada;
    }

    public void setEpisodiosPorTemporada(int episodiosPorTemporada) {
        this.episodiosPorTemporada = episodiosPorTemporada;
    }

    public void setMinutosPorEpisodios(int minutosPorEpisodios) {
        this.minutosPorEpisodios = minutosPorEpisodios;
    }

    public int getMinutosPorEpisodios() {
        return minutosPorEpisodios;
    }

    @Override
    public void exibirFichaTecnica() {
        System.out.printf("""
                          ----------- Ficha Técnica -----------
                          Título: %s
                          Ano de Lançamento: %d
                          Está concluída: %b
                          Temporadas: %d
                          Episódios por Temporada: %d
                          Minutos por episódio: %d
                          Duração em Minutos: %d
                          Média de Avaliações: %.1f
                          Incluso no plano: %s
                          """, getNome(), getAnoLancamento(), ativo, temporadas, episodiosPorTemporada, minutosPorEpisodios, getDuracaoMinutos(), calcularMedia(), inclusoPlano());
    }

    @Override
    public int getDuracaoMinutos() {
        return temporadas * episodiosPorTemporada * minutosPorEpisodios;
    }

}
