import br.com.alura.screenmatch.modelos.Filme;

public class Main {
    public static void main(String[] args) {
        Filme filme = new Filme("Kpop Demon Hunters", 2025, 95, true );

        filme.avaliar(10);
        filme.avaliar(9);
        filme.avaliar(9);
        filme.avaliar(8);
        filme.avaliar(10);
        filme.avaliar(10);

        filme.exibirFichaTecnica();
    }
}
