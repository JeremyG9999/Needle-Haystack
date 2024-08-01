import random
class NeedleHaystack:
    def __init__(self):
        self.incorrect_guesses = 0
        self.correct_guesses = 0
        self.peeked = 0
        self.losses = 0
    def reset_game(self):
        self.hay = random.randint(1, 100)
        self.attempts = 6
        self.peek_attempts = 3
    def guess(self):
        while True:
            guesses = int(input("\nTry to guess my number between 1 and 100 to find the needle in the haystack: "))
            if guesses > 100 or guesses < 1:
                print("\nPick a number in the range")
                continue
            if guesses == self.hay:
                print("\nYou found it!!!!")
                self.correct_guesses += 1
                self.reset_game()
                break
            else:
                self.attempts -= 1
                self.incorrect_guesses += 1
                if self.attempts == 0:
                    print(f"\nYou failed! The answer was {self.hay}")
                    self.losses += 1
                    self.reset_game()
                    break
                else:
                    print(f"\nWrong guess! You have {self.attempts} guess attempts left.")
                    if self.peek_attempts > 0:
                        print(f"You have {self.peek_attempts} peek attempts left")
                        choice = input("Would you like to take a peek: Y/N: ")
                        if choice.upper() == "Y":
                            self.peeked += 1
                            self.take_a_peek()
                            self.peek_attempts -= 1
                    else:
                        print("No more peek attempts left for this game session.")
                        continue
    def take_a_peek(self):
        if self.peek_attempts == 3:
            peek_range = random.randint(15, 20)
        elif self.peek_attempts == 2:
            peek_range = random.randint(8, 12)
        else:
            peek_range = random.randint(1, 3)
        lower_bound = max(1, self.hay - peek_range)
        upper_bound = min(100, self.hay + peek_range)
        print(f"\nPeek: The number is between {lower_bound} and {upper_bound}")
    def statistics(self):
        print(f"\nYou have {self.correct_guesses} correct guesses.")
        print(f"You have {self.incorrect_guesses} incorrect guesses.")
        total_guesses = self.correct_guesses + self.incorrect_guesses
        print(f"You have made {total_guesses} total guesses.")
        print(f"You peeked {self.peeked} times.")
        print(f"You lost {self.losses} times!!!\n")
        if self.losses > self.correct_guesses:
            print("You have more losses than correct guesses, failure!")
        elif self.correct_guesses > self.losses:
            print("You probably relied on the hints to stay ahead of me!")
        elif self.incorrect_guesses or self.correct_guesses == 0:
            print("Would you hurry up and play already!!!")
        else:
            print("Tie ball game, but it would not be if you didn't use so many hints!")
    def rules(self):
        print("\n1. When you press play game you will be prompted to enter a number")
        print("2. That will be your first of 6 guesses")
        print("3. If you guess correctly before your attempts reach 0 you win, if not you lose")
        print("4. After each guess attempt is incorrect you will be asked if you want to use a hint")
        print("5. It is wise to use them all ASAP because you cannot use them continuously without making a guess first")
        print("6. Be sure to use your guesses ASAP so you have as many attempts to get the correct answer as you can")
    def main_menu(self):
        self.reset_game()
        while True:
            print("\nWelcome to the Main Menu: ")
            print("1. Play the game!!!")
            print("2. Statistics")
            print("3. Rules")
            print("4. Exit")
            choice = input("\nSelect a choice: ")
            if choice == "1":
                self.guess()
            elif choice == "2":
                self.statistics()
            elif choice == "3":
                self.rules()
            elif choice == "4":
                break
            else:
                print("\nPlease enter a number between 1 and 4")
def main():
    run = NeedleHaystack()
    run.main_menu()
main()