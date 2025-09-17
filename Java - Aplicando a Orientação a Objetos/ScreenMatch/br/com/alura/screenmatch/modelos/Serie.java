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

    public int getMinutosPorEpisodios() {
        return minutosPorEpisodios;
    }

    public void setMinutosPorEpisodios(int minutosPorEpisodios) {
        this.minutosPorEpisodios = minutosPorEpisodios;
    }

    @Override
    public int getDuracaoMinutos() {
        return temporadas * episodiosPorTemporada * minutosPorEpisodios;
    }
}
