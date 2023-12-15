package animais;


//gato - > sub classe
// Animal - > super classe
public class Gato extends Animal {
    public Gato(String nome){
        super(nome);
    }

    public void miar(){
        System.out.printf("%s miou\n", getNome());
    }
}
