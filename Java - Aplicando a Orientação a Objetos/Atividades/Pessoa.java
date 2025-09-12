public class Pessoa {
    public static void falar() {
        System.out.println("Olá, mundo");
    }

    public static void main(String[] args) {
        // Por se tratar de uma classe estática não precisamos utilizar o "new"
        // Não possui estado, somente lógica
        // É utilizada para funções auxiliares (Math, Collections, etc)
        // Os métodos não dependem de atributos do objeto
        Pessoa.falar();
    }
}
