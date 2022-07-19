import java.util.Random;
import java.util.Scanner;

/*
 Title: Rock Paper Scissors
 */
class Main {
  public static void main(String[] args) {
    for (;;) {
      play();
    }
  }

  static void play() {
    String[] choices = { "rock", "paper", "scissors" };
    String userChoice = getUserInput().toLowerCase();
    Random random = new Random();
    int randomInt = random.nextInt(3);
    String cpuChoice = choices[randomInt];
    getResult(cpuChoice, userChoice);
  }

  static void getResult(String cpuChoice, String userChoice) {
    String winConditions = "rockpaperscissorsrock";
    System.out.println("CPU picked: " + cpuChoice);
    // win/lose/draw
    if (cpuChoice.equals(userChoice)) {
      System.out.println("Draw!");
    } else if (winConditions.contains(cpuChoice + userChoice)) {
      System.out.println("You win!");
    } else {
      System.out.println("You lose!");
    }
    System.out.println();
  }

  static String getUserInput() {
    Scanner input = new Scanner(System.in);
    try {
      System.out.println("Rock, Paper, Scissors: ");
      String userChoice = input.nextLine();
      return userChoice;
    } finally {
        // input.close(); // Resource leak?
    }
  }
}
