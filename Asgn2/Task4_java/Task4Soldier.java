/*
 * CSCI3180 Principles of Programming Languages
 *
 * --- Declaration ---
 *
 * I declare that the assignment here submitted is original except for source
 * material explicitly acknowledged. I also acknowledge that I am aware of
 * University policy and regulations on honesty in academic work, and of the
 * disciplinary guidelines and procedures applicable to breaches of such policy
 * and regulations, as contained in the website
 * http://www.cuhk.edu.hk/policy/academichonesty/
 *
 * Assignment 2
 * Name : Lee Tsz Yan
 * Student ID : 1155110177
 * Email Addr : tylee8@cse.cuhk.edu.hk
 */

import java.util.HashSet;
import java.util.Random;

public class Task4Soldier extends Soldier{
  private int coin;
  private int shield;

  public Task4Soldier() {
    super();
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
  public boolean loseHealth() {
    int h = this.shield > 2? 0: (10 - 5 * (this.shield));
    this.health -= h;
    return this.health <= 0;
  } 

  @Override
  public void displayInformation() {
    super.displayInformation();
    System.out.printf("Defence: %d.%n", this.shield * 5);
    System.out.printf("Coins: %d.%n", this.coin);
  }
}