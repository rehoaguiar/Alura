import br.com.alura.screenmatch.calculos.CalculadoraDeTempo;
import br.com.alura.screenmatch.calculos.FiltroRecomendacao;
import br.com.alura.screenmatch.modelos.Episodio;
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

        Serie serie = new Serie("Jujutsu Kaisen", 2020, 3, 23,23, true, true);
        serie.exibirFichaTecnica();

        Episodio episodio = new Episodio();
        episodio.setNumero(1);
        episodio.setNome("Ryomen Sukuna");
        episodio.setSerie(serie);
        episodio.setTotalVisualizacoes(10000);

        episodio.exibirFichaTecnica();

        // Código Omitido
        CalculadoraDeTempo calculadora = new CalculadoraDeTempo();
        calculadora.inclui(filme);
        calculadora.inclui(serie);

        FiltroRecomendacao filtro = new FiltroRecomendacao();
        filtro.filtra(filme);
        filtro.filtra(episodio);
    }
}