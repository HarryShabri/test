import java.util.Scanner;

class Hapus{
  public void hapus(){
    System.out.print("\033[H\033[2J");  
    System.out.flush();
  }
}
class karakter{
  public String username , weapon; 
  public int health , armor , attack;
  public void buatkarakter(String username, String weapon, int health,int armor,int attack){
      this.username = username;
      this.weapon = weapon;
      this.health = health;
      this.armor = armor;
      this.attack = attack;
  }
  public void infoplayer1(){
    System.out.println("INFO PLAYER 1 : ");
    System.out.println("Nama      : "+this.username);
    System.out.println("Senjata   : "+this.weapon);
    System.out.println("Darah     : "+this.health);
    System.out.println("Ketahanan : "+this.armor);
    System.out.println("Serangan  : "+this.attack);
  }
  public void infoplayer2(){
    System.out.println("INFO PLAYER 2 : ");
    System.out.println("Nama      : "+this.username);
    System.out.println("Senjata   : "+this.weapon);
    System.out.println("Darah     : "+this.health);
    System.out.println("Ketahanan : "+this.armor);
    System.out.println("Serangan  : "+this.attack);
  }
  public void serang (karakter lawan){
    System.out.println(this.username+" menyerang "+lawan.username);
    int damage = this.attack - lawan.armor;
    System.out.println(lawan.username+" terkena damage sebesar "+damage);
    int sisa_darah = lawan.health - damage;
    lawan.health = sisa_darah;
    System.out.println("darah "+lawan.username+" tersisa "+lawan.health);
  }
  }

public class latihan {
  public static void main(String[]args){
    Scanner input = new Scanner(System.in);
    karakter player1 = new karakter();
    Hapus kosong = new Hapus();
    System.out.print("BUAT KARAKTER");
    System.out.println("");
    System.out.print("Masukkan nama : ");
    player1.username = input.nextLine();
    System.out.print("Masukkan nama senjata : " );
    player1.weapon = input.nextLine();
    player1.buatkarakter(player1.username, player1.weapon, 100, 15, 50);
    kosong.hapus();
    karakter player2 = new karakter();
    System.out.print("BUAT KARAKTER");
    System.out.println("");
    System.out.print("Masukkan nama : ");
    player2.username = input.nextLine();
    System.out.print("Masukkan nama senjata : ");
    player2.weapon = input.nextLine();
    player2.buatkarakter(player2.username, player2.weapon,100, 20, 60);
    kosong.hapus();
    player1.infoplayer1();
    player2.infoplayer2();
    kosong.hapus();
    int pertandingan = 0;
    while(pertandingan < 11){
      player1.serang(player2);
      player2.serang(player1);
      pertandingan ++;
      kosong.hapus();
    }
    if(player1.health>player2.health){
      System.out.println("player 1 win");
      player1.infoplayer1();
    }else {
        System.out.println("Player 2 win");
        player2.infoplayer2();
    }

  }
}