package br.com.alura.screenmatch.calculos;

import br.com.alura.screenmatch.modelos.Titulo;

public class CalculadoraDeTempo {
    private int tempoTotal;

    public void inclui(Titulo titulo) {
        System.out.printf("Adicionando a duração em minutos de %s em sua lista de reprodução", titulo);
        this.tempoTotal += titulo.getDuracaoMinutos();
    }

    public int getTempoTotal() {
        return tempoTotal;
    }


}
