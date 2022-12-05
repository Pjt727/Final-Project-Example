from random import randint; num: int = randint(1, 10); guess_is_num: callable = lambda g: True if g == num else False; guesses: list[int] = [None]
while not guess_is_num(guesses[-1]): user_input: str = input("Guess a number 1-10: "); guesses.append(int(user_input)) if user_input.isnumeric() else print("That is not a positive integer");
print(f"You guessed the correct number in {len(guesses)-1} guesses... here were your guesses {' '.join(map(str, guesses[1:]))}")
