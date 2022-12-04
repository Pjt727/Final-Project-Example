from random import randint

lower_bound, upper_bound = (1, 10,) # 1-10 hardcoded 

class BadInput(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)



class GuessingGame:
    '''Structure for guessing an integer within a range'''
    def __init__(self, lower_bound: int, upper_bound: int) -> None:
        self.lower_bound: int = lower_bound
        self.upper_bound: int = upper_bound
    
    def guess_num(self) -> None:
        '''Game loop to guess number until guessed'''
        self.num: int = randint(self.lower_bound, self.upper_bound)
        self.guesses: list[int] = []
        while True:
            try:
                guess: str = input("Guess a number 1-10: ")
                is_guessed: bool = self.guess_is_num(guess)
            except BadInput as error:
                print(error)
                continue
            self.guesses.append(int(guess))
            if not is_guessed:
                print("WRONG!")
                continue
            break

        print(f"You guessed the correct number in {len(self.guesses)} guesses.")
        print(f"Your guesses were {' '.join(map(str, self.guesses))}")

    def guess_is_num(self, input: str) -> bool:
        if not input.isnumeric():
            raise BadInput("Your input is not a positive integer.")
        input = int(input)
        if input not in range(self.lower_bound, self.upper_bound + 1):
            raise BadInput(f"Your input is not between {self.lower_bound} and {self.upper_bound}.")
        if input in self.guesses:
            raise BadInput("Your input has already been guessed.")
        
        return input == self.num



def main() -> None:
    global lower_bound, upper_bound
    game: GuessingGame = GuessingGame(lower_bound, upper_bound)
    game.guess_num()

if __name__ == "__main__":
    main()
