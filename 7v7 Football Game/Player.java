import java.util.*;
 


class Player{

  protected String name, currentTeam;

  protected String color;
  protected int number;
  protected String teamColor;
  public int x,y;
  


 


  public Player(String name, String color, int number, int x, int y, String currentTeam){

    this.currentTeam = currentTeam;
    this.name = name;
    this.color = color;
    this.number = number;
   
    this.x=x;
    this.y=y;
    
  }


  public String toString(){
    return name + "// Current Team: " + currentTeam;
  }



  public void setY(int newY){
    y=newY;
  }

  public void setX(int newX){
    x=newX;
  }

  public int getX(){
    return x;
  }

  public int jersey(){
    return number;
  }
  
  public int getY(){
    return y;
  }
  public void drawPlayer(){
    System.out.print(color + number);
  }
  public String getName(){
    return name;
  }
}







  
