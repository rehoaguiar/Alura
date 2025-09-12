public class IdadePessoa {
    private String nome;
    private int idade;

    // Getters e Setters
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

   // Métodos
   public void verificarIdade() {
        if (idade < 18) {
            System.out.printf("-> %s é menor de idade\n", getNome());

        } else {
            System.out.printf("-> %s é maior de idade\n", getNome());

        }
   }

    // Main
    public static void main(String[] args) {
        IdadePessoa idadePessoa1 = new IdadePessoa();

        idadePessoa1.setNome("Anne");
        idadePessoa1.setIdade(22);

        System.out.printf("\nNome: %s", idadePessoa1.getNome());
        System.out.printf("\nIdade: %d\n", idadePessoa1.getIdade());

        idadePessoa1.verificarIdade();

        IdadePessoa idadePessoa2 = new IdadePessoa();

        idadePessoa2.setNome("Samuel");
        idadePessoa2.setIdade(10);

        System.out.printf("\nNome: %s", idadePessoa2.getNome());
        System.out.printf("\nIdade: %d\n", idadePessoa2.getIdade());

        idadePessoa2.verificarIdade();
    }
}
