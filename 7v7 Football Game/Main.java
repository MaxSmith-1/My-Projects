import java.util.Scanner;

//sound imports
import java.util.*;

import javazoom.jl.player.Player;
import java.io.FileInputStream;





class Main {
  public static void main(String[] args) {
  Team c = new Team("Bombers");
  Team b = new Team("Robbers");

    Drive e = new Drive(c,b,18,6);
    //playing music

try {
      // create a FileInputStream from the MP3 file
      FileInputStream fis = new FileInputStream("nfl.mp3");

      // create a Player object from the FileInputStream
      Player player = new Player(fis);

      // play the MP3 file
      player.play(2);
    } catch (Exception q) {
      // handle any errors
      q.printStackTrace();
    }    

//14 yards for td

    
  System.out.println("Welcome to 7v7 football! \nIn this league, all players are equally skilled, leaving the job of winning soley upon you, the coach and head statistician\n\nBefore playing, you must pick your squad\n");
    c.pickTeam(b);
    e.n();

}


}
