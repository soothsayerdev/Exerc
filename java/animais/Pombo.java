package animais;

public class Pombo extends Ave{
    private int cartasEnviadas;

    public Pombo(String nome){
        super(nome);
        cartasEnviadas = 10;
    }

    public void entregarCartas(){
        System.out.printf("%s esta entregando cartas\n", getNome());
        cartasEnviadas++;
        //this.cartasEnviadas = cartasEnviadas + 1;
    }
    public void pruh(){
        System.out.printf("%s esta a fazer PRUH!\n", getNome());
        System.out.printf("");
    }

    public int getCartasEnviadas() {
        return cartasEnviadas;
    }
    
}
