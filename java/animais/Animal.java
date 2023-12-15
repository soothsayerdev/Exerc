package animais;

public class Animal {
    private String nome;

    public Animal(String nome){
        this.nome = nome;
    }


    public void comer(){
        // <NOME> comeu
        String mensagem = String.format("%s comeu", nome);
        System.out.printf("%s comeu\n", nome);
        System.out.println(mensagem);
    }

    public void beber(){
        System.out.printf("%s bebeu\n", nome);        
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    
}
