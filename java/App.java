import animais.Cachorro;
import animais.Dragao;
import animais.Gato;
import animais.Pombo;

public class App {
    public static void main(String[] args) throws Exception{
        Cachorro cachorro = new Cachorro("Caramelo");
        // cachorro.setNome("Caramelo");
        cachorro.latir();
        cachorro.comer();

        Gato gato = new Gato("Digas");
        // gato.setNome("Digas");
        gato.miar();

        Dragao dragao = new Dragao("Banguela");
        // dragao.setNome("Banguela");
        dragao.cuspirFogo();
        dragao.voar();

        Pombo pombo = new Pombo("Pombo Correio");
        // pombo.setNome("Xandre");
        pombo.voar();
        pombo.entregarCartas();
        pombo.pruh();
    }
}