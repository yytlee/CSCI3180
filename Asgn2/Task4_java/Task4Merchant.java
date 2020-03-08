import java.util.Scanner;

public class Task4Merchant {
  private int elixirPrice;
  private int shieldPrice;
  private Pos pos;

  public Task4Merchant(int elixirPrice, int shieldPrice) {

    // TODO: Initialization.
    this.elixirPrice = elixirPrice;
    this.shieldPrice = shieldPrice;
    this.pos = new Pos();
  }

  public void actionOnSoldier(Task4Soldier soldier) {
    this.talk("Do you want to buy something? (1. Elixir, 2. Shield) Input: ");

    // TODO: Main logic.
    Scanner sc = new Scanner(System.in);
    String choice = sc.nextLine();

    if (choice.equalsIgnoreCase("1")) {
      if (soldier.getNumCoin() >= elixirPrice){
        soldier.useCoin(elixirPrice);
        soldier.addElixir();
        System.out.printf("You have %d coin(s) left.%n", soldier.getNumCoin());
      } else {
        this.talk("Poor guy, you don't have enough coins.%n");
      }
    } else if (choice.equalsIgnoreCase("2")) {
      if(soldier.getNumCoin() >= shieldPrice) {
        soldier.useCoin(shieldPrice);
        soldier.addShield();
        System.out.printf("You have %d coin(s) left.%n", soldier.getNumCoin());
      } else {
        this.talk("Poor guy, you don't have enough coins.%n");
      }
    } else {
      System.out.printf("=> Illegal move!%n%n");
    }

  }

  public void talk(String text) {
    System.out.printf("Merchant$: " + text);
  }

  // TODO: Other functions.

  public Pos getPos() {
    return this.pos;
  }

  public void setPos(int row, int column) {
    this.pos.setPos(row, column);
  }

  public void displaySymbol() {
    System.out.printf("$");
  }
}