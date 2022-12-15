import java.util.*;

class Player {

  // Name and Current NFL Team of player
  protected String name, currentTeam;
  // Jersey Color (i.e, the font color on the field)
  protected String color;
  // Jersey Number
  protected int number;

  // Starting coordinates when the field is drawn
  public int x, y;

  // Constructor for a Player.
  public Player(String name, String color, int number, int x, int y, String currentTeam) {

    this.currentTeam = currentTeam;
    this.name = name;
    this.color = color;
    this.number = number;

    this.x = x;
    this.y = y;

  }

  // This method returns the Name and Current Team of a player.
  public String toString() {
    return name + "// Current Team: " + currentTeam;
  }

  // This method sets the player's Y coordinate.
  public void setY(int newY) {
    y = newY;
  }

  // This method sets the player's X coordinate.
  public void setX(int newX) {
    x = newX;
  }

  // This method returns the player's X coordinate.
  public int getX() {
    return x;
  }

  // This method returns the player's jersey number.
  public int jersey() {
    return number;
  }

  // This method returns the player's Y coordinate.
  public int getY() {
    return y;
  }

  // This method prints the player's number that player's font color.
  public void drawPlayer() {
    System.out.print(color + number);
  }

  // This method returns the player's name.
  public String getName() {
    return name;
  }
}
