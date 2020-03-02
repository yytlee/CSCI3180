import java.util.Scanner;

public class Merchant {
  private int elixirPrice;
  private int shieldPrice;
  private Pos pos;

  public Merchant() {
    // TODO: Initialization.
  }

  public void actionOnSoldier(NewSoldier soldier) {
    this.talk("Do you want to buy something? (1. Elixir, 2. Shield) Input: ");

    // TODO: Main logic.

  }

  public void talk(String text) {
    System.out.printf("Merchant$: " + text);
  }

  // TODO: Other functions.
}