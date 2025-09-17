package br.com.alura.screenmatch.calculos;

import br.com.alura.screenmatch.modelos.Titulo;

public class CalculadoraDeTempo {
    private int tempoTotal;

    public void inclui(Titulo titulo) {
        System.out.printf("%n Adicionando a duração em minutos de %s em sua lista de reprodução", titulo.getNome());
        this.tempoTotal += titulo.getDuracaoMinutos();
    }

    public int getTempoTotal() {
        return tempoTotal;
    }


}
