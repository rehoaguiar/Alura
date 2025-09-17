package br.com.alura.screenmatch.calculos;

public class FiltroRecomendacao {

    public void filtra(Classificavel classificavel) {
        if (classificavel.getClassificacao() >= 4) {
            System.out.printf("%n%s está entre os preferidos do momento ", classificavel.getNome());
        } else if (classificavel.getClassificacao() >= 2) {
            System.out.printf("%n%s está muito bem avaliado no momento ", classificavel.getNome());
        } else {
            System.out.printf("%nColoque %s na sua lista para assistir depois ", classificavel.getNome());
        }
    }
}
