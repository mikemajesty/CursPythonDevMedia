import time;
import random;
name = input("What's your name? ");
print("Hello, "+ name," Time to Play Hangname!\n");
time.sleep(1);
print("Start guessing......");
time.sleep(0.5);

listOfWords = ("devdedia","mike","lima","tode","ibiuna");
randomNumer = random.randint(0,len(listOfWords) - 1);
guessWord = listOfWords[randomNumer];
word = guessWord;
guesses = "";
turns = 10;
while turns > 0:
    failed = 0;
    for char in word:
        if char in guesses:
           print(char);
        else:
            print("_");
            failed += 1;

    if failed == 0:
        print("\n You win");
        break;
    print;
    guess = input("guess a character: ");
    guesses += guess.lower();
    if guess not in word:
            turns -= 1;
            print("Wrong\n");
            print("You have ", turns, "more guesses");
            if turns == 0:
                print("You Lose\n");



