import java.util.HashSet;
import java.util.Random;

abstract class Soldier {
  private int health;
  private int numElixirs;
  private Pos pos;
  private HashSet<Integer> keys;

  public Soldier() {
    this.health = 100;
    this.numElixirs = 2;
    this.pos = new Pos();
    this.keys = new HashSet<Integer>();
    /* It is possible for the soldier to obtain two identical keys in the game.
       To simplify the operation, we use set here to remove duplicate keys. */
  }

  public int getHealth() {
    return this.health;
  }

  public boolean loseHealth() {
    this.health -= 10;
    return this.health <= 0;
  }

  public void recover(int healingPower) {
    /* Soldier's health cannot exceed capacity. */
    int totalHealth = healingPower + this.health;
    this.health = totalHealth >= 100 ? 100 : totalHealth;
  }

  public Pos getPos() {
    return this.pos;
  }

  public void setPos(int row, int column) {
    this.pos.setPos(row, column);
  }

  public void move(int row, int column) {
    this.setPos(row, column);
  }

  public HashSet<Integer> getKeys() {
    return this.keys;
  }

  public void addKey(int key) {
    this.keys.add(key);
  }

  public int getNumElixirs() {
    return this.numElixirs;
  }

  public void addElixir() {
    this.numElixirs += 1;
  }

  public void useElixir() {
    Random random = new Random();
    this.recover(random.nextInt(6) + 15);
    this.numElixirs -= 1;
  }

  public void displayInformation() {
    System.out.printf("Health: %d.%n", this.health);
    System.out.printf("Position (row, column): (%d, %d).%n", this.pos.getRow(), this.pos.getColumn());
    System.out.printf("Keys: " + this.keys + ".%n");
    System.out.printf("Elixirs: %d.%n", this.numElixirs);
  }

  public void displaySymbol() {
    System.out.printf("S");
  }
}

public class Task4Soldier extends Soldier{
  private int health;
  private int coin;
  private int shield;

  public Task4Soldier() {
    super();
    this.health = 100;
    this.coin = 0;
    this.shield = 0;
  }

  public int getNumCoin() {
    return this.coin;
  }

  public void addCoin() {
    this.coin += 1;
  }

  public void useCoin(int n) {
    this.coin -= n;
  }

  public void addShield() {
    this.shield += 1;
  }

  @Override
  public int getHealth() {
    return this.health;
  }

  @Override
  public boolean loseHealth() {
    int h = this.shield > 2? 0: (10 - 5 * (this.shield));
    this.health -= h;
    return this.health <= 0;
  } 

  @Override
  public void recover(int healingPower) {
    /* Soldier's health cannot exceed capacity. */
    int totalHealth = healingPower + this.health;
    this.health = totalHealth >= 100 ? 100 : totalHealth;
  }

  @Override
  public void displayInformation() {
    System.out.printf("Health: %d.%n", this.health);
    System.out.printf("Position (row, column): (%d, %d).%n", super.getPos().getRow(), super.getPos().getColumn());
    System.out.printf("Keys: " + super.getKeys() + ".%n");
    System.out.printf("Elixirs: %d.%n", super.getNumElixirs());
    System.out.printf("Defence: %d.%n", this.shield);
    System.out.printf("Coins: %d.%n", this.coin);
  }
}