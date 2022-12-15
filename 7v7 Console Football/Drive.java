
import java.util.*;
//import java.util.concurrent.TimeUnit;

// enter valid number error glitch johnson
//receiver input safe

class Drive {

  // Tracks what down it is
  protected int downs;
  // 2 different teams
  protected Team a;
  protected Team b;
  // Coordinates of football
  protected int fbx, fby;
  // Tracks how many drives have been completed
  protected int drives;
  // The score
  protected int mypoints, otherPoints;

  // Constructor for drive, takes two teams and the starting coordinates for the
  // football
  public Drive(Team a, Team b, int fbx, int fby) {
    this.a = a;
    this.b = b;
    this.fbx = 18;
    this.fby = 6;
    this.downs = 1;
    this.drives = 6;

  }

  // This method runs a passing play.
  public void pass() {
    Scanner in = new Scanner(System.in);
    boolean u = true;
    // 14 yards for a touchdown
    int bigPlayYardage = (int) (Math.random() * 4) + 10;
    int smallPlayYardage = (int) (Math.random() * 4) + 1;

    // the while loop catches input errors
    while (u) {

      System.out.println();
      System.out.println(
          "Which pass: \n1. Deep Pass - 50% chance of a big play, 50% chance of incompletion or interception\n2. Medium Pass - 25% chance of a big play, 50% chance of small play, 25% chance of incompletion or interception \n3. Screen -12.5% chance of a big play, 75% chance of small play, 12.5% chance of incompletion or tunover");
      String d = in.nextLine();
      System.out.print("\033[H\033[2J");
      System.out.flush();

      if (d.equals("1")) {
        // little easter egg here... if the number one receiver is juiced, it is an
        // automatic big play regardless of odds
        int juicedReceiver = ((int) (Math.random() * 5) + 1);
        // random number that determines outcome of play
        int deepProb = ((int) (Math.random() * 100) + 1);

        boolean v = true;
        int e = 0;
        String k = "";

        while (v) {
          System.out.println("Which receiver should we target?\n1." + a.roster()[1].getName() + "\n2."
              + a.roster()[2].getName() + "\n3." + a.roster()[3].getName() + "\n4." + a.roster()[4].getName() + "\n5."
              + a.roster()[5].getName());
          k = in.nextLine();

          if (k.equals("1") || k.equals("2") || k.equals("3") || k.equals("4") || k.equals("5")) {
            v = false;
          } else {
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("Enter a valid number");
          }
        }
        e = Integer.parseInt(k);
        // notifies player of "juiced receiver"

        if (juicedReceiver == 1) {
          System.out.println("(Just got word from the offensive coordinator... " + a.roster()[juicedReceiver].getName()
              + " likes his matchup...)");
        }
        // if the #1 receier is "juiced" or it the random deepProb integer is above 50,
        // it is a big play
        if ((e == juicedReceiver) || (deepProb >= 50)) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.print("Big Play!");
          // redraw
          // i is x: we are only moving along the x
          // j is y

          // this block moves the receiver and ball up the field "bigPlayYardage" amount
          // of yards
          int tempx = a.roster()[e].getX();
          int tempy = a.roster()[e].getY();
          a.roster()[e].setX(tempx - bigPlayYardage);
          a.roster()[e].setY(tempy);
          fbx = (a.roster()[e].getX() - 1);
          fby = a.roster()[e].getY();
          // checking to make sure player doesn't "run out of endzone"
          if (a.roster()[e].getX() < 4) {
            a.roster()[e].setX(3);
            fbx = 2;
          }

          // this block redraws the field to show the big play for 6 seconds
          field();
          try {
            Thread.sleep(6000);
          } catch (InterruptedException z) {
            Thread.currentThread().interrupt();
          }
          // crowd noise? 3 types, one for each type of play

          // the entire team moves to the spot of the play, the field is redrawn, and the
          // function ends
          System.out.print("\033[H\033[2J");
          System.out.flush();

          System.out.println();
          System.out.println();
          System.out.println();

          a.roster()[e].setX(tempx);
          a.roster()[e].setY(tempy);
          a.moveTheChains(bigPlayYardage);

          fby = a.roster()[0].getY();
          fbx = a.roster()[0].getX() - 1;
          field();
        }

        // if deepProb is less than 50, it is either an imcompletion or interception,
        // 50/50 chance
        else if (deepProb < 50) {

          int f = (int) (Math.random() * 2);
          if (f == 0) {

            // no gain
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("Incomplete Pass");
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException z) {
              Thread.currentThread().interrupt();
            }
          }
          if (f == 1) {

            // a
            downs = 5;
            System.out.print("Interception... the other team takes over");

            // if its an interception, the team is reset to their origional positions and
            // the other team takes over
            a.roster()[0].setX(19);
            a.roster()[1].setX(18);
            a.roster()[2].setX(18);
            a.roster()[3].setX(18);
            a.roster()[4].setX(19);
            a.roster()[5].setX(18);
            try {

              Thread.sleep(6000);
            } catch (InterruptedException z) {
              Thread.currentThread().interrupt();
            }

            System.out.print("\033[H\033[2J");
            System.out.flush();

          }
        }
        u = false;
      }

      // the next two input types (2 for Medium Pass, 3 for screen pass) use the same
      // moving/drawing functions. The only difference between the three is the odds
      // of a big play/small play/incompletion or turnover happening

      else if (d.equals("2")) {

        boolean v = true;
        int e = 0;
        String k = "";
        while (v) {
          System.out.println("Which receiver should we target?\n1." + a.roster()[1].getName() + "\n2."
              + a.roster()[2].getName() + "\n3." + a.roster()[3].getName() + "\n4." + a.roster()[4].getName() + "\n5."
              + a.roster()[5].getName());

          k = in.nextLine();

          if (k.equals("1") || k.equals("2") || k.equals("3") || k.equals("4") || k.equals("5")) {
            v = false;
          } else {
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("Enter a valid number");
          }
        }
        e = Integer.parseInt(k);
        int midProb = (int) (Math.random() * 100) + 1;

        if (midProb < 25) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.print("Big Play!");
          // redraw
          // i is x: we are only moving along the x
          // j is y
          int tempx = a.roster()[e].getX();
          int tempy = a.roster()[e].getY();
          a.roster()[e].setX(tempx - bigPlayYardage);
          a.roster()[e].setY(tempy);
          fbx = (a.roster()[e].getX() - 1);
          fby = a.roster()[e].getY();
          // checking to make sure player doesn't "run out of endzone"
          if (a.roster()[e].getX() < 4) {
            a.roster()[e].setX(3);
            fbx = 2;
          }
          field();
          try {
            Thread.sleep(6000);
          } catch (InterruptedException z) {
            Thread.currentThread().interrupt();
          }
          // crowd noise? 3 types, one for each type of play
          System.out.print("\033[H\033[2J");
          System.out.flush();

          System.out.println();
          System.out.println();
          System.out.println();
          a.roster()[e].setX(tempx);
          a.roster()[e].setY(tempy);
          a.moveTheChains(bigPlayYardage);

          fby = a.roster()[0].getY();
          fbx = a.roster()[0].getX() - 1;
          field();
        } else if ((midProb > 25) && (midProb < 75)) {
          System.out.println("Small gain..");
          int tempx = a.roster()[e].getX();
          int tempy = a.roster()[e].getY();
          a.roster()[e].setX(tempx - smallPlayYardage);
          a.roster()[e].setY(tempy + 2);
          fbx = (a.roster()[e].getX() - 1);
          fby = a.roster()[e].getY();
          // checking to make sure player doesn't "run out of endzone"
          if (a.roster()[e].getX() < 4) {
            a.roster()[e].setX(3);
            fbx = 2;
          }
          field();
          try {
            Thread.sleep(6000);
          } catch (InterruptedException w) {
            Thread.currentThread().interrupt();
          }
          // crowd noise? 3 types, one for each type of play
          System.out.print("\033[H\033[2J");
          System.out.flush();

          System.out.println();
          System.out.println();
          System.out.println();
          a.roster()[e].setX(tempx);
          a.roster()[e].setY(tempy);
          a.moveTheChains(smallPlayYardage);

          fby = a.roster()[0].getY();
          fbx = a.roster()[0].getX() - 1;
          field();

        }

        else {
          int b = (int) (Math.random() * 2);

          if (b == 0) {
            downs = 6;
            System.out.println("Interception... the other team has taken over");
            a.roster()[0].setX(19);
            a.roster()[1].setX(18);
            a.roster()[2].setX(18);
            a.roster()[3].setX(18);
            a.roster()[4].setX(19);
            a.roster()[5].setX(18);
            try {
              Thread.sleep(6000);
            } catch (InterruptedException z) {
              Thread.currentThread().interrupt();
            }
            System.out.print("\033[H\033[2J");
            System.out.flush();
          }
          if (b == 1) {
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("Incomplete Pass");
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException z) {
              Thread.currentThread().interrupt();
            }
          }
        }
        u = false;
      }

      else if (d.equals("3")) {

        boolean v = true;
        int e = 0;
        String k = "";
        while (v) {
          System.out.println("Which receiver should we target?\n1." + a.roster()[1].getName() + "\n2."
              + a.roster()[2].getName() + "\n3." + a.roster()[3].getName() + "\n4." + a.roster()[4].getName() + "\n5."
              + a.roster()[5].getName());

          k = in.nextLine();

          if (k.equals("1") || k.equals("2") || k.equals("3") || k.equals("4") || k.equals("5")) {
            v = false;
          } else {
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("Enter a valid number");
          }

        }
        e = Integer.parseInt(k);
        int screenProb = (int) (Math.random() * 100) + 1;

        if (screenProb < 13) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.print("Big Play!");
          // redraw
          // i is x: we are only moving along the x
          // j is y
          int tempx = a.roster()[e].getX();
          int tempy = a.roster()[e].getY();
          a.roster()[e].setX(tempx - bigPlayYardage);
          a.roster()[e].setY(tempy);
          fbx = (a.roster()[e].getX() - 1);
          fby = a.roster()[e].getY();
          // checking to make sure player doesn't "run out of endzone"
          if (a.roster()[e].getX() < 4) {
            a.roster()[e].setX(3);
            fbx = 2;
          }
          field();
          try {
            Thread.sleep(6000);
          } catch (InterruptedException z) {
            Thread.currentThread().interrupt();
          }
          // crowd noise? 3 types, one for each type of play
          System.out.print("\033[H\033[2J");
          System.out.flush();

          System.out.println();
          System.out.println();
          System.out.println();
          a.roster()[e].setX(tempx);
          a.roster()[e].setY(tempy);
          a.moveTheChains(bigPlayYardage);

          fby = a.roster()[0].getY();
          fbx = a.roster()[0].getX() - 1;
          field();
        } else if ((screenProb > 13) && (screenProb < 89)) {
          System.out.println("Small gain..");
          int tempx = a.roster()[e].getX();
          int tempy = a.roster()[e].getY();
          a.roster()[e].setX(tempx - smallPlayYardage);
          a.roster()[e].setY(tempy + 2);
          fbx = (a.roster()[e].getX() - 1);
          fby = a.roster()[e].getY();
          // checking to make sure player doesn't "run out of endzone"
          if (a.roster()[e].getX() < 4) {
            a.roster()[e].setX(3);
            fbx = 2;
          }
          field();
          try {
            Thread.sleep(6000);
          } catch (InterruptedException w) {
            Thread.currentThread().interrupt();
          }
          // crowd noise? 3 types, one for each type of play
          System.out.print("\033[H\033[2J");
          System.out.flush();

          System.out.println();
          System.out.println();
          System.out.println();
          a.roster()[e].setX(tempx);
          a.roster()[e].setY(tempy);
          a.moveTheChains(smallPlayYardage);

          fby = a.roster()[0].getY();
          fbx = a.roster()[0].getX() - 1;
          field();

        }

        else {
          int b = (int) (Math.random() * 2);

          if (b == 0) {
            downs = 6;
            System.out.println("Interception... the other team has taken over");
            a.roster()[0].setX(19);
            a.roster()[1].setX(18);
            a.roster()[2].setX(18);
            a.roster()[3].setX(18);
            a.roster()[4].setX(19);
            a.roster()[5].setX(18);
            try {
              Thread.sleep(6000);
            } catch (InterruptedException z) {
              Thread.currentThread().interrupt();
            }
            System.out.print("\033[H\033[2J");
            System.out.flush();

          }
          if (b == 1) {
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("Incomplete Pass");
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException z) {
              Thread.currentThread().interrupt();
            }
          }
        }
        u = false;
      }

      else {

        System.out.println("Enter a valid number");
      }
    }
  }

  // This method runs a running play.
  public void run() {

    /// Three scenarios: 1. No gain 2. Short Gain 3. Home Run
    Scanner in = new Scanner(System.in);

    int op = ((int) (Math.random() * 9) + 1) * 10;

    int ip = ((int) (Math.random() * 9) + 1) * 10;

    int sp = ((int) (Math.random() * 9) + 1) * 10;

    // 14 yards for a touchdown
    int bigPlayYardage = (int) (Math.random() * 4) + 10;
    int smallPlayYardage = (int) (Math.random() * 4) + 1;
    boolean q = true;
    while (q) {
      System.out.println("Which run: \n1. Outside Zone - " + op + "% chance of a big play\n2. Inside Zone - " + ip
          + "% chance of a big play\n3. Jet Sweep - " + sp + "% chance of big play");
      String d = in.nextLine();
      System.out.print("\033[H\033[2J");
      System.out.flush();

      if (d.equals("1")) {

        int c = ((int) (Math.random() * 99 + 1));
        System.out.println(c);
        if (c <= op) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.print("Big Play!");
          // redraw
          // i is x: we are only moving along the x
          // j is y
          int tempx = a.roster()[4].getX();
          int tempy = a.roster()[4].getY();
          a.roster()[4].setX(tempx - bigPlayYardage);
          a.roster()[4].setY(tempy + 6);
          fbx = (a.roster()[4].getX() - 1);
          fby = a.roster()[4].getY();
          // checking to make sure player doesn't "run out of endzone"
          if (a.roster()[4].getX() < 4) {
            a.roster()[4].setX(3);
            fbx = 2;
          }
          field();
          try {
            Thread.sleep(6000);
          } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
          }
          // crowd noise? 3 types, one for each type of play
          System.out.print("\033[H\033[2J");
          System.out.flush();

          System.out.println();
          System.out.println();
          System.out.println();
          a.roster()[4].setX(tempx);
          a.roster()[4].setY(tempy);
          a.moveTheChains(bigPlayYardage);

          fby = a.roster()[0].getY() - 1;
          fbx = a.roster()[0].getX() - 1;
          field();

        } else {
          int b = (int) (Math.random() * 2);
          if (b == 0) {
            System.out.println("Small gain..");
            int tempx = a.roster()[4].getX();
            int tempy = a.roster()[4].getY();
            a.roster()[4].setX(tempx - smallPlayYardage);
            a.roster()[4].setY(tempy + 6);
            fbx = (a.roster()[4].getX() - 1);
            fby = a.roster()[4].getY();
            // checking to make sure player doesn't "run out of endzone"
            if (a.roster()[4].getX() < 4) {
              a.roster()[4].setX(3);
              fbx = 2;
            }
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
            }
            // crowd noise? 3 types, one for each type of play
            System.out.print("\033[H\033[2J");
            System.out.flush();

            System.out.println();
            System.out.println();
            System.out.println();
            a.roster()[4].setX(tempx);
            a.roster()[4].setY(tempy);
            a.moveTheChains(smallPlayYardage);

            fby = a.roster()[0].getY() - 1;
            fbx = a.roster()[0].getX() - 1;
            field();

          }
          if (b == 1) {
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("No gain");
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
            }
          }
        }
        q = false;
      }

      else if (d.equals("2")) {

        int c = ((int) (Math.random() * 99 + 1));
        System.out.println(c);
        if (c <= ip) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.print("Big Play!");
          // redraw
          // i is x: we are only moving along the x
          // j is y
          int tempx = a.roster()[4].getX();
          int tempy = a.roster()[4].getY();
          a.roster()[4].setX(tempx - bigPlayYardage);
          a.roster()[4].setY(tempy);
          fbx = (a.roster()[4].getX() - 1);
          fby = a.roster()[4].getY();
          // checking to make sure player doesn't "run out of endzone"
          if (a.roster()[4].getX() < 4) {
            a.roster()[4].setX(3);
            fbx = 2;
          }
          field();
          try {
            Thread.sleep(6000);
          } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
          }
          // crowd noise? 3 types, one for each type of play
          System.out.print("\033[H\033[2J");
          System.out.flush();

          System.out.println();
          System.out.println();
          System.out.println();
          a.roster()[4].setX(tempx);
          a.roster()[4].setY(tempy);
          a.moveTheChains(bigPlayYardage);

          fby = a.roster()[0].getY() - 1;
          fbx = a.roster()[0].getX() - 1;
          field();

        } else {
          int b = (int) (Math.random() * 2);
          if (b == 0) {
            System.out.println("Small gain..");
            int tempx = a.roster()[4].getX();
            int tempy = a.roster()[4].getY();
            a.roster()[4].setX(tempx - smallPlayYardage);
            a.roster()[4].setY(tempy);
            fbx = (a.roster()[4].getX() - 1);
            fby = a.roster()[4].getY();
            // checking to make sure player doesn't "run out of endzone"
            if (a.roster()[4].getX() < 4) {
              a.roster()[4].setX(3);
              fbx = 2;
            }
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
            }
            // crowd noise? 3 types, one for each type of play
            System.out.print("\033[H\033[2J");
            System.out.flush();

            System.out.println();
            System.out.println();
            System.out.println();
            a.roster()[4].setX(tempx);
            a.roster()[4].setY(tempy);
            a.moveTheChains(smallPlayYardage);

            fby = a.roster()[0].getY() - 1;
            fbx = a.roster()[0].getX() - 1;
            field();

          }
          if (b == 1) {
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("No gain");
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
            }
          }
        }
        q = false;
      }

      else if (d.equals("3")) {

        int c = ((int) (Math.random() * 99 + 1));
        System.out.println(c);
        if (c <= sp) {
          System.out.print("\033[H\033[2J");
          System.out.flush();
          System.out.print("Big Play!");
          // redraw
          // i is x: we are only moving along the x
          // j is y
          int tempx = a.roster()[2].getX();
          int tempy = a.roster()[2].getY();
          a.roster()[2].setX(tempx - bigPlayYardage);
          a.roster()[2].setY(tempy + 10);
          fbx = (a.roster()[2].getX() - 1);
          fby = a.roster()[2].getY();
          // checking to make sure player doesn't "run out of endzone"
          if (a.roster()[2].getX() < 2) {
            a.roster()[2].setX(3);
            fbx = 2;
          }
          field();
          try {
            Thread.sleep(6000);
          } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
          }
          // crowd noise? 3 types, one for each type of play
          System.out.print("\033[H\033[2J");
          System.out.flush();

          System.out.println();
          System.out.println();
          System.out.println();
          a.roster()[2].setX(tempx);
          a.roster()[2].setY(tempy);
          a.moveTheChains(bigPlayYardage);

          fby = a.roster()[0].getY() - 1;
          fbx = a.roster()[0].getX() - 1;
          field();

        } else {
          int b = (int) (Math.random() * 2);
          if (b == 0) {
            System.out.println("Small gain..");
            int tempx = a.roster()[2].getX();
            int tempy = a.roster()[2].getY();
            a.roster()[2].setX(tempx - smallPlayYardage);
            a.roster()[2].setY(tempy);
            fbx = (a.roster()[2].getX() - 1);
            fby = a.roster()[2].getY();
            // checking to make sure player doesn't "run out of endzone"
            if (a.roster()[2].getX() < 4) {
              a.roster()[2].setX(3);
              fbx = 2;
            }
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
            }
            // crowd noise? 3 types, one for each type of play
            System.out.print("\033[H\033[2J");
            System.out.flush();

            System.out.println();
            System.out.println();
            System.out.println();
            a.roster()[2].setX(tempx);
            a.roster()[2].setY(tempy);
            a.moveTheChains(smallPlayYardage);

            fby = a.roster()[0].getY() - 1;
            fbx = a.roster()[0].getX() - 1;
            field();

          }
          if (b == 1) {

            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("No gain");
            field();
            try {
              Thread.sleep(6000);
            } catch (InterruptedException e) {
              Thread.currentThread().interrupt();
            }

          }
        }
        q = false;
      }

      else {
        System.out.println("Enter a valid number");
      }

    }
  }

  // This method runs a trick play.
  public void trickPlay() {
    Scanner in = new Scanner(System.in);

    System.out.print("\033[H\033[2J");
    System.out.flush();
    int trickProb = (int) (Math.random() * 10) + 1;
    int randPos = (int) (Math.random() * 6);

    if (trickProb == 2) {
      // touchdown
      int tempx = a.roster()[randPos].getX();
      a.roster()[randPos].setX(2);
      fbx = (a.roster()[randPos].getX() - 1);
      fby = a.roster()[randPos].getY();
      System.out.println("\"You have got to be kidding me.... that might just be the greatest catch I've ever seen\""
          + "\n - Chris Collinsworth");
      field();
      try {
        Thread.sleep(6000);
      } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
      }
      // crowd noise? 3 types, one for each type of play
      System.out.print("\033[H\033[2J");
      System.out.flush();

    } else {
      if (trickProb % 2 == 1) {
        System.out.print("\033[H\033[2J");
        System.out.flush();
        System.out.println("No gain");
        field();
        try {
          Thread.sleep(6000);
        } catch (InterruptedException e) {
          Thread.currentThread().interrupt();
        }
      }
      if (trickProb % 2 == 0) {
        downs = 6;
        System.out.println("Turnover... the other team takes over");
        fbx = 18;
        fby = 6;
        a.roster()[0].setX(19);
        a.roster()[1].setX(18);
        a.roster()[2].setX(18);
        a.roster()[3].setX(18);
        a.roster()[4].setX(19);
        a.roster()[5].setX(18);
      }
    }
  }

  // This method draws the field with your team and defenders
  public void field() {

    String GREEN = "\033[0;32m"; // GREEN
    String BLACK = "\033[0;30m"; // BLACK
    String RED = "\033[0;31m"; // RED

    String YELLOW = "\033[0;33m"; // YELLOW
    String BLUE = "\033[0;34m"; // BLUE
    String PURPLE = "\033[0;35m"; // PURPLE
    String CYAN = "\033[0;36m"; // CYAN
    String WHITE = "\033[0;37m"; // WHITE

    for (int i = 0; i < 25; i++) {

      System.out.println();

      for (int j = 0; j < 16; j++) {

        if ((i == 0) || (i == 24)) {
          System.out.print(WHITE + "■■");
        }
        // qb OUR TEAM
        else if (i == a.roster()[0].getX() && j == a.roster()[0].getY()) {
          a.roster()[0].drawPlayer();
          System.out.print(GREEN + "■");
        }

        else if (i == fbx && j == fby) {
          System.out.print(GREEN + "🏈");
        }
        // rb
        else if (i == a.roster()[4].getX() && j == a.roster()[4].getY()) {
          a.roster()[4].drawPlayer();
        }
        // wrs = 18 , (1,3,13)
        else if (i == a.roster()[1].getX() && j == a.roster()[1].getY()) {
          a.roster()[1].drawPlayer();
        } else if (i == a.roster()[2].getX() && j == a.roster()[2].getY()) {
          a.roster()[2].drawPlayer();
        }

        else if (i == a.roster()[3].getX() && j == a.roster()[3].getY()) {
          a.roster()[3].drawPlayer();
        }
        // te = 18,9
        else if (i == a.roster()[5].getX() && j == a.roster()[5].getY()) {
          a.roster()[5].drawPlayer();
        }

        // DEFENSE, Linebackers
        else if (i == a.roster()[0].getX() - 3 && j == a.roster()[0].getY()) {

          System.out.print(RED + "X");
          if (a.roster()[0].getX() - 2 < 4) {
            System.out.print(YELLOW + "■");
          } else {
            System.out.print(GREEN + "■");
          }
        }

        else if (i == a.roster()[4].getX() - 3 && j == a.roster()[4].getY()) {
          System.out.print(RED + "X");
          if (a.roster()[4].getX() - 2 < 4) {
            System.out.print(YELLOW + "■");
          } else {
            System.out.print(GREEN + "■");
          }
        }
        // DBs
        else if (i == a.roster()[1].getX() - 2 && j == a.roster()[1].getY()) {
          System.out.print(RED + "X");
          if (a.roster()[1].getX() - 2 < 4) {
            System.out.print(YELLOW + "■");
          } else {
            System.out.print(GREEN + "■");
          }
        } else if (i == a.roster()[2].getX() - 2 && j == a.roster()[2].getY()) {
          System.out.print(RED + "X");
          if (a.roster()[2].getX() - 2 < 4) {
            System.out.print(YELLOW + "■");
          } else {
            System.out.print(GREEN + "■");
          }
        }

        else if (i == a.roster()[3].getX() - 2 && j == a.roster()[3].getY()) {
          System.out.print(RED + "X");
          if (a.roster()[3].getX() - 2 < 4) {
            System.out.print(YELLOW + "■");
          } else {
            System.out.print(GREEN + "■");
          }
        }
        // te = 18,9
        else if (i == a.roster()[5].getX() - 2 && j == a.roster()[5].getY() + 1) {
          System.out.print(RED + "X");
          if (a.roster()[5].getX() - 2 < 4) {
            System.out.print(YELLOW + "■");
          } else {
            System.out.print(GREEN + "■");
          }
        }

        // END DEFENSE

        else if ((j == 0)) {
          System.out.print(WHITE + "■" + GREEN + "■");
        } else if ((j == 15)) {
          System.out.print(GREEN + "■" + WHITE + "■");
        } else if (i == fbx) {
          System.out.print(BLUE + "■■");
        } else if ((i < 4)) {
          System.out.print(YELLOW + "■■");
        } else if (i > 20) {
          System.out.print(PURPLE + "■■");
        } else if ((j == 4) || (j == 12)) {
          System.out.print(WHITE + "■" + GREEN + "■");
        }

        else {
          System.out.print(GREEN + "■■");
        }
      }
    }

  }

  // This method tracks the downs and score and prompts the user to choose a
  // play. If the downs exceede 4, this method turns the ball over to the other
  // team. If the ball's x-value (fbx) is in the endzone, this method outputs
  // "Touchdown" and gives the ball to the other team
  public void play() {
    String GREEN = "\033[0;32m"; // GREEN

    Scanner in = new Scanner(System.in);

    while (downs < 5) {
      System.out.print("\033[H\033[2J");
      System.out.flush();
      field();
      System.out.println();
      System.out.println();
      // protected int mypoints, otherPoints;
      System.out.println();
      System.out.println();
      System.out.println("Score: \n" + a.teamName() + ": " + mypoints + "\n" + b.teamName() + ": " + otherPoints);
      System.out.println();
      System.out.println();
      System.out.println("Drive: " + drives + "/4");
      System.out.println("Down: " + downs + "\n...you need 14 yards (this is a new type of field)");
      System.out.println(
          "You're the coach of the " + a.teamName() + ": \n1.Run\n2.Pass\n3.Trick Play (If you're feeling bold)");

      String w = in.nextLine();

      if (w.equals("1")) {
        System.out.print("\033[H\033[2J");
        System.out.flush();
        field();
        run();
        downs++;
      } else if (w.equals("2")) {
        System.out.print("\033[H\033[2J");
        System.out.flush();
        field();

        pass();
        downs++;
      } else if (w.equals("3")) {
        System.out.print("\033[H\033[2J");
        System.out.flush();
        field();

        trickPlay();
        downs++;
      } else {
        System.out.print("\033[H\033[2J");
        System.out.flush();
        System.out.println("Enter a valid number");
      }

      if (fbx <= 4) {
        downs = 1;
        mypoints += 7;
        System.out.print("\033[H\033[2J");
        System.out.flush();

        System.out.println(GREEN + "Touchdown!!!");
        System.out.println();
        System.out.println();
        System.out.println("Score: \n" + a.teamName() + ": " + mypoints + "\n" + b.teamName() + ": " + otherPoints);
        fbx = 18;
        fby = 6;
        a.roster()[0].setX(19);
        a.roster()[1].setX(18);
        a.roster()[2].setX(18);
        a.roster()[3].setX(18);
        a.roster()[4].setX(19);
        a.roster()[5].setX(18);

        try {
          Thread.sleep(3000);
        } catch (InterruptedException e) {
          Thread.currentThread().interrupt();
          System.out.print("\033[H\033[2J");
          System.out.flush();
        }
        System.out.print("\033[H\033[2J");
        System.out.flush();
        break;

      }

    }

    if (downs == 5) {
      System.out.print("\033[H\033[2J");
      System.out.flush();
      System.out.print("Turnover on downs... the other team takes possession");
      System.out.println();
      System.out.println();
      System.out.println("Score: \n" + a.teamName() + ": " + mypoints + "\n" + b.teamName() + ": " + otherPoints);

      fbx = 18;
      fby = 6;
      a.roster()[0].setX(19);
      a.roster()[1].setX(18);
      a.roster()[2].setX(18);
      a.roster()[3].setX(18);
      a.roster()[4].setX(19);
      a.roster()[5].setX(18);

      try {
        Thread.sleep(3000);
      } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
        System.out.print("\033[H\033[2J");
        System.out.flush();
      }

      downs = 1;
    }

  }

  // This method simulates the other team playing on offense
  public void otherTeamPlays() {

    String RED = "\033[0;31m"; // RED
    System.out.println(RED + "The " + b.teamName() + " take the field");

    downs = 1;
    fbx = 18;
    int yl = fbx;
    while (downs < 5) {
      int playCall = (int) (Math.random() * 2);
      int prob = (int) (Math.random() * 10);
      int gain = (int) (Math.random() * 10);

      if (playCall == 0) {
        System.out.println("The " + b.teamName() + " run the ball...");
        try {
          Thread.sleep(3000);
        } catch (InterruptedException e) {
          Thread.currentThread().interrupt();
        }

      } else if (playCall == 1) {
        System.out.println("The " + b.teamName() + " pass the ball...");
        try {
          Thread.sleep(3000);
        } catch (InterruptedException e) {
          Thread.currentThread().interrupt();
        }
      }
      System.out.println("... and gain " + gain + " yards");
      System.out.println();
      try {
        Thread.sleep(3000);
      } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
      }
      fbx -= gain;

      if (fbx <= 4) {
        System.out.println();
        System.out.println("Touchdown " + b.teamName());
        System.out.println();
        System.out.println();
        otherPoints += 7;
        System.out.println("Score: \n" + a.teamName() + ": " + mypoints + "\n" + b.teamName() + ": " + otherPoints);
        try {
          Thread.sleep(3000);
        } catch (InterruptedException e) {
          Thread.currentThread().interrupt();
        }
        System.out.print("\033[H\033[2J");
        System.out.flush();

        downs = 1;
        break;
      }
      downs++;
    }

    if (downs == 5) {
      System.out.println("The " + b.teamName() + " turns the ball over on downs");
      downs = 1;
      try {
        Thread.sleep(3000);
      } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
      }
      System.out.print("\033[H\033[2J");
      System.out.flush();
    }
    fbx = 18;
    downs = 1;
  }

  // This method manages the game: you play 4 times and the computer plays 4
  // times. At the end of the game, it compares your score with the computer's
  // score and outputs a final result (Win,loss, or tie).
  public void n() {

    String GREEN = "\033[0;32m"; // GREEN

    String RED = "\033[0;31m"; // RED
    drives = 1;
    while (drives < 5) {
      play();
      otherTeamPlays();
      drives++;
    }

    System.out.print("\033[H\033[2J");
    System.out.flush();
    // protected int mypoints, otherPoints;
    if (mypoints > otherPoints) {
      System.out.println(
          GREEN + "Final Score: " + "\n" + a.teamName() + " - " + mypoints + "\n" + b.teamName() + " - " + otherPoints);
      System.out.println("“A champion is simply someone who did not give up when he wanted to.”\n\n- Tom Landry");
    } else if (otherPoints > mypoints) {
      System.out.println(
          RED + "Final Score: " + "\n" + a.teamName() + " - " + mypoints + "\n" + b.teamName() + " - " + otherPoints);
      System.out.println("\"We did't loose the game... we just ran out of time\"\n\n- Vince Lombardi");
    } else if (otherPoints == mypoints) {
      System.out.println(
          "Final Score: " + "\n" + a.teamName() + " - " + mypoints + "\n" + b.teamName() + " - " + otherPoints);
      System.out.println("\"I didn't even know you could tie in the NFL\" \n\n-Najee Harris, last year");
    }
  }

}
