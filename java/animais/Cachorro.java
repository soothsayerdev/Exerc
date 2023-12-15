package animais;

public class Cachorro extends Animal {
    // private int ossosComidos;

    public Cachorro(String nome){
        super(nome); // -> primeira linha contem a chamada do construtor SUPER
        // this.ossosComidos = 10;
    }

    public void latir(){
        System.out.printf("%s latiu", getNome());
    }

    public void lamber(){
        System.out.printf("%s lambeu", getNome());
    }
}
