public class Musica {
    String titulo;
    String artista;
    double somaNotas;
    int anoLancamento;
    int numAvaliacoes;

    public void avaliarMusica(double nota) {
        somaNotas += nota;
        numAvaliacoes++;
    }

    public double calcularMedia() {
         double mediaAvaliacoes = somaNotas / numAvaliacoes;
         return Math.round(mediaAvaliacoes * 10.00) / 10.00;
    }

    public void exibirFichaTecnica() {
        System.out.printf("""
                        --------- Informações Técnicas ---------
                        Título: %s
                        Artista: %s
                        Ano de Lançamento: %s
                        Média das Avaliações: %.1f
                        ----------------------------------------
                        """, titulo, artista, anoLancamento, calcularMedia());
    }

    // Main
    public static void main(String[] args) {
        // Classes de Instância precisar do "new" para conseguirmos utilizar os seus métodos e atributos
        // Cada objeto terá o seu próprio estado
        // É utilizado para modelar entidades (Pessoa, Carro, etc)
        // Métodos acessam atributos desse objeto

        // Instanciando a nossa classe
        // O parentheses ficará vazio, pois não temos um construtor nessa classe
        Musica musica = new Musica();

        // Se houvesse um construtor, poderíamos inicializar os dados diretamente dentro do parentheses
        musica.titulo = "Where to Go";
        musica.artista = "DeAngelo";
        musica.anoLancamento = 2025;

        musica.avaliarMusica(10);
        musica.avaliarMusica(9.5);
        musica.avaliarMusica(8);

        musica.exibirFichaTecnica();
    }
}
