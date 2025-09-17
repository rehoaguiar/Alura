import br.com.alura.screenmatch.modelos.Filme;
import br.com.alura.screenmatch.modelos.Serie;

public class Main {
    public static void main(String[] args) {
        Filme filme = new Filme("Kpop Demon Hunters", "Maggie Kang e Chris Appelhans", 2025, 95, true );

        filme.avaliar(10);
        filme.avaliar(9);
        filme.avaliar(9);
        filme.avaliar(8);
        filme.avaliar(10);
        filme.avaliar(10);

        filme.exibirFichaTecnica();

        Serie serie = new Serie("Jujutsu Kaiser", 2020, 3, 23,23, true, true);
        System.out.println(serie.getDuracaoMinutos());
    }
}