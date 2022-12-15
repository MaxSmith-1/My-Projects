import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    // Two teams are initiated, yours being the "Bombers" and the computer's being
    // the "Robbers."
    Team c = new Team("Bombers");
    Team b = new Team("Robbers");

    // A drive is initiated with the two teams and the starting coordinates for the
    // football
    Drive e = new Drive(c, b, 18, 6);

    // Initial remarks are made.
    System.out.println(
        "Welcome to 7v7 football! \nIn this league, all players are equally skilled, leaving the job of winning soley upon you, the coach and head statistician\n\nBefore playing, you must pick your squad\n");
    // The user picks a team.
    c.pickTeam(b);
    // The game starts.
    e.n();

  }

}
