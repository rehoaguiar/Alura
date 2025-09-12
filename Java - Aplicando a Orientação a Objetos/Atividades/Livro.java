public class Livro {
    private String titulo;
    private String autor;

    // Getters e Setters
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    // Métodos
    public void exibirDetalhes() {
        System.out.printf("""
                          \n---------------------------------
                          Título: %s
                          Autor: %s
                          ---------------------------------
                          """, getTitulo(), getAutor());
    }

    // Main
    public static void main(String[] args) {
        Livro livro = new Livro();

        livro.setTitulo("Oppa, Foi Mal");
        livro.setAutor("N.S. Park");

        livro.exibirDetalhes();

        livro.setTitulo("Sonho de Um Dia de Verão");
        livro.setAutor("N.S. Park");

        livro.exibirDetalhes();

        livro.setTitulo("Prometa Não Se Apaixonar");
        livro.setAutor("N.S. Park");

        livro.exibirDetalhes();
    }
}
