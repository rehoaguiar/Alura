public class Aluno {
    private String nome;
    private double nota1, nota2, nota3;

    // Construtor


    public Aluno(String nome, double nota1, double nota2, double nota3) {
        this.nome = nome;
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
    }

    // Getters e Setters
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getNota1() {
        return nota1;
    }

    public void setNota1(double nota1) {
        this.nota1 = nota1;
    }

    public double getNota2() {
        return nota2;
    }

    public void setNota2(double nota2) {
        this.nota2 = nota2;
    }

    public double getNota3() {
        return nota3;
    }

    public void setNota3(double nota3) {
        this.nota3 = nota3;
    }

    // Métodos
    public double calcularMedia() {
        return (nota1 + nota2 + nota3) / 3;
    }

    // Main
    public static void main(String[] args) {
        Aluno aluno1 = new Aluno("Samuel", 10, 8.5, 9);
        Aluno aluno2 = new Aluno("Alice", 10, 4, 7);
        Aluno aluno3 = new Aluno("Gabriel", 5, 4, 7);

        System.out.printf("""
                           \n--------------- Aluno 1 ---------------
                           Nome: %s
                           Nota 1: %.2f
                           Nota 2: %.2f
                           Nota 3: %.2f
                           Média: %.2f
                           ---------------------------------------
                          """, aluno1.getNome(), aluno1.getNota1(), aluno1.getNota2(), aluno1.getNota3(), aluno1.calcularMedia());

        System.out.printf("""
                           \n--------------- Aluno 2 ---------------
                           Nome: %s
                           Nota 1: %.2f
                           Nota 2: %.2f
                           Nota 3: %.2f
                           Média: %.2f
                           ---------------------------------------
                          """, aluno2.getNome(), aluno2.getNota1(), aluno2.getNota2(), aluno2.getNota3(), aluno2.calcularMedia());

        System.out.printf("""
                           \n--------------- Aluno 3 ---------------
                           Nome: %s
                           Nota 1: %.2f
                           Nota 2: %.2f
                           Nota 3: %.2f
                           Média: %.2f
                           ---------------------------------------
                          """, aluno3.getNome(), aluno3.getNota1(), aluno3.getNota2(), aluno3.getNota3(), aluno3.calcularMedia());
    }
}
