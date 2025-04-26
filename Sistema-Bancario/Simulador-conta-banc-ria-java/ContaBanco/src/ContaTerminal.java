import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) throws Exception {
      

       int numero = 1021;
       String agencia = "067-8";
       String nomeCliente = "MARIO ANDRE";
       double saldo = 237.48;

        //TODO: Conhecer e importar a classe Scanner
        Scanner scanner = new Scanner(System.in);

        //Exibir as mensagens para o nosso usuário
        System.out.println("Olá. Bem vindo ao Banco Masterx!");
       

        //Obter pelo scannner os valores digitados no terminal
        System.out.println("Digite o número da sua conta");
        String nome = scanner.nextLine();

        //Exibir a mensagem conta criada
        if (nome == nome) {
            System.out.println("Olá " + nomeCliente + ", obrigado por criar uma conta em nosso banco, sua agência é " + agencia + 
            ",conta " + numero + " e seu saldo " + saldo + " já está disponível para saque");
        }
        else {
           System.out.println("Número da conta é inválido"); 
        }


    }
}