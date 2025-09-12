public class Carro {
    String marca;
    String modelo;
    String cor;
    int ano;

    // Construtor
    public Carro(String marca, String modelo, String cor, int ano){
        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
    }

    public int calcularIdade() {
        return (2025 - ano);
    }

    public void exibirInformacoes() {
        System.out.printf("""
                        --------- Informações Técnicas ---------
                        Marca: %s
                        Modelo: %s
                        Cor: %s
                        Ano: %d
                        Idade: %d anos
                        ----------------------------------------
                        """, marca, modelo, cor, ano, calcularIdade());
    }

    // Main
    public static void main(String[] args) {
        // Utilizando um construtor não precisamos abstrair as informações
        // Visto que ele mesmo já inicializa os atributos com os valores fornecidos
        Carro carro = new Carro("Honda", "Civic G10", "Preto", 2025 );

        carro.exibirInformacoes();
    }
}
