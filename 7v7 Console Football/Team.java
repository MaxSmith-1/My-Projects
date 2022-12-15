import java.util.Scanner;
import java.util.Arrays;

//update all players with X and Y coords
class Team {

  // Scanner is initiated.
  Scanner in = new Scanner(System.in);
  // Team name
  protected String name;
  // List of 6 players on a Team
  protected Player[] a = new Player[6];

  // ASKI color values
  public String GREEN = "\033[0;32m"; // GREEN
  public String BLACK = "\033[0;30m"; // BLACK
  public String RED = "\033[0;31m"; // RED
  public String YELLOW = "\033[0;33m"; // YELLOW
  public String BLUE = "\033[0;34m"; // BLUE
  public String PURPLE = "\033[0;35m"; // PURPLE
  public String CYAN = "\033[0;36m"; // CYAN
  public String WHITE = "\033[0;37m"; // WHITE

  // Constructor for Team.
  public Team(String name) {
    this.name = name;

  }

  // This method prompts the user to choose a quarterback and adds that player to
  // Player array a.
  public void pickQB() {

    // picking quarterbacks
    // qb x,y: 19,6
    //
    Player qb1 = new Player("Lamar Jackson", PURPLE, 8, 19, 6, "Ravens");
    Player qb2 = new Player("Tua", CYAN, 1, 19, 6, "Dolphins");
    System.out.println("Pick a quarterback: \n 1. " + qb1.toString() + "\n 2. " + qb2.toString());
    String b = in.nextLine();
    if (b.equals("1")) {
      a[0] = qb1;
      System.out.println("Your quarterback is " + a[0].getName());

    } else if (b.equals("2")) {
      a[0] = qb2;
      System.out.println("Your quarterback is " + a[0].getName());

    }
  }

  // This method prompts the user to choose three wide receivers and adds all
  // three to Player array a.
  public void pickWR() {

    // picking receivers

    // wrs = 18 , (1,3,13)
    int start1 = 1;
    int start2 = 3;
    int start3 = 13;
    Player wr1 = new Player("Justin Jefferzyn", PURPLE, 18, 18, 0, "Vikings");
    Player wr2 = new Player("Tyreek Hill", CYAN, 10, 18, 0, "Dolphins");
    Player wr3 = new Player("Dhop", RED, 10, 18, 0, "Cardinals");
    Player wr4 = new Player("Olave", YELLOW, 12, 18, 0, "Saints");
    Player wr5 = new Player("Diggs", BLUE, 14, 18, 0, "Bills");
    Player wr6 = new Player("Kadarius Toney", RED, 19, 18, 0, "Chiefs");
    Player fill = new Player("fill", "asdf", 0, 0, 0, "Denver Broncos");

    // System.out.print("\033[H\033[2J");
    // System.out.flush();
    System.out.println("Pick 3 wide receivers: \n 1. " + wr1.toString() + "\n 2. " + wr2.toString() + "\n 3. "
        + wr3.toString() + "\n 4. " + wr4.toString() + "\n 5. " + wr5.toString() + "\n 6. " + wr6.toString());
    String f = in.nextLine();
    String g = in.nextLine();
    String h = in.nextLine();

    int c = Integer.parseInt(f);
    int d = Integer.parseInt(g);
    int e = Integer.parseInt(h);
    Player[] wrList = new Player[] { wr1, wr2, wr3, wr4, wr5, wr6 };
    int wrCount = 1;
    int owrCount = 1;
    for (int i = 0; i < wrList.length; i++) {
      if ((c - 1 == (i)) || (d - 1 == (i)) || (e - 1 == (i))) {
        a[wrCount] = wrList[i];
        wrList[i] = fill;
        if (wrCount == 1) {
          a[wrCount].setY(1);
        }

        else if (wrCount == 2) {
          a[wrCount].setY(3);
        } else if (wrCount == 3) {
          a[wrCount].setY(13);
        }
        wrCount++;
      }

      if (wrCount >= 4) {
        break;
      }
    }

  }

  // This method prompts the user to choose a running back and adds that player to
  // Player array a.
  public void pickRB() {

    Player rb1 = new Player("Pacheco", RED, 10, 19, 8, "Chiefs");
    Player rb2 = new Player("Pollard", BLUE, 20, 19, 8, "Cowboys");
    System.out.println("Pick a running back: \n 1. " + rb1.toString() + "\n 2. " + rb2.toString());
    String z = in.nextLine();
    if (z.equals("1")) {
      a[4] = rb1;
      System.out.println("Your running back is " + a[4].getName());
    } else if (z.equals("2")) {
      a[4] = rb2;
      System.out.println("Your running back is " + a[4].getName());

    }

  }

  // This method prompts the user to choose a tight end and adds that player to
  // Player array a.
  public void pickTE() {

    Player te1 = new Player("Pat Freiermuth", YELLOW, 88, 18, 9, "Steelers");
    Player te2 = new Player("Travis Kelce", RED, 87, 18, 9, "Chiefs");
    System.out.println("Pick a tight end: \n 1. " + te1.toString() + "\n 2. " + te2.toString());
    String y = in.nextLine();
    if (y.equals("1")) {
      a[5] = te1;
      System.out.println("Your tight end is " + a[5].getName());

    } else if (y.equals("2")) {
      a[5] = te2;
      System.out.println("Your tight end is " + a[5].getName());

    }

    System.out.print("\033[H\033[2J");
    System.out.flush();

  }

  // This method calls the previous "pick" functions in order and asks the user to
  // "Enter a valid number" when an invalid input is entered.
  public void pickTeam(Team other) {

    boolean l = false;

    boolean z = false;
    boolean t = false;

    pickQB();
    if (a[0] == null) {
      l = true;
      while (l) {
        if (a[0] == null) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.println("Please enter a valid number: ");
          pickQB();
        } else {
          l = false;
        }
      }
    }

    boolean h = false;
    System.out.print("\033[H\033[2J");
    System.out.flush();

    h = true;
    while (h) {
      try {
        pickWR();
      } catch (NumberFormatException e) {
        System.out.print("\033[H\033[2J");
        System.out.flush();
        System.out.println("Please enter valid numbers: ");
      }
      if (a[1] != null && a[2] != null && a[3] != null) {
        h = false;
      }
    }

    System.out.print("\033[H\033[2J");
    System.out.flush();

    // RB = 19,8

    pickRB();
    if (a[4] == null) {
      t = true;
      while (t) {
        if (a[4] == null) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.println("Please enter a valid number: ");
          pickRB();
        } else {
          t = false;
        }
      }
    }
    System.out.print("\033[H\033[2J");
    System.out.flush();

    pickTE();
    if (a[5] == null) {
      z = true;
      while (z) {
        if (a[5] == null) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.println("Please enter a valid number: ");
          pickTE();
        } else {
          z = false;
        }
      }
    }
    // picking tight end

    // te = 18,9

    System.out.println("\nYour Roster: ");
    for (Player x : a) {
      System.out.println(x.getName());
    }

    /*
     * System.out.println("\nOpponent's Roster: ");
     * for(Player x : othersPlayers){
     * System.out.println(x.getName());
     * }
     * 
     */
  }

  // This method returns the list of players on a Team.
  public Player[] roster() {
    return a;
  }

  // This method moves each player on a Team "yardage" yards up the field.
  public void moveTheChains(int yardage) {
    for (Player x : a) {
      x.setX(x.getX() - yardage);
    }
  }

  // This method returns the name of the Team.
  public String teamName() {
    return name;
  }
}
