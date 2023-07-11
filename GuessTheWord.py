import random

# This function takes a word and scrabbles it by
# separating the letters into a list and
# rejoining the letters
def scrabble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# This function turns the word in to a list 
# to be more legible
def turn_word_into_list(word):
    return list(word)

# List of random words to pick from
def play_game():
    list_of_random_words = [
    'regret', 'crib', 'cheer', 'invite', 'manage', 'meek', 'warn', 'fat', 'want',
    'prickly', 'crawl', 'ready', 'black', 'surprise', 'remind', 'imminent', 'painful',
    'include', 'maddening', 'stale', 'spiders', 'limping', 'heady', 'moor', 'challenge', 
    'applaud', 'hurried', 'treatment', 'bomb', 'shirt', 'bucket', 'sincere', 'cuddly', 
    'trains', 'extra-large', 'crowd', 'classy', 'peace', 'load', 'rings', 'soggy', 'pocket', 
    'crow', 'attempt', 'sisters', 'pin', 'nation', 'green', 'jagged', 'lowly', 'explain', 
    'mix', 'shake', 'thoughtful', 'motion', 'tiny', 'lumpy', 'blood', 'garrulous', 'son', 
    'frightening', 'cure', 'ducks', 'flash', 'flippant', 'defeated', 'homeless', 'fire', 
    'reflective', 'feeling', 'clover', 'twist', 'confused', 'disagree', 'doubt', 'polite', 
    'thank', 'tick', 'voyage', 'distinct', 'smoke', 'faithful', 'scratch', 'invention', 'stage', 
    'scribble', 'passenger', 'psychedelic', 'effect', 'unlock', 'stay', 'morning', 'attraction', 
    'nappy', 'eager', 'therapeutic', 'drop', 'trick', 'teeth', 'sort', 'productive', 'trucks', 
    'title', 'duck', 'childlike', 'seed', 'lying', 'spare', 'actually', 'grubby', 'harbor', 'vessel', 
    'sigh', 'afternoon', 'past', 'striped', 'gamy', 'fence', 'mere', 'attach', 'aboard', 'resonant', 
    'donkey', 'poke', 'omniscient', 'heap', 'part', 'edge', 'day', 'dear', 'grateful', 'chalk', 'iron', 
    'hop', 'squirrel', 'burst', 'sticks', 'gullible', 'enormous', 'fertile', 'oven', 'bad', 'ice', 
    'absorbed', 'division', 'gun', 'earsplitting', 'neat', 'sidewalk', 'obsequious']

    # Prompts the user for their name
    # and greets them
    name = input("Hello, what is your name? ")
    print(f"Hello, {name}! Let's see how many words you can guess.")

    correct_guesses = 0

    while True:

        # Chooses a random word from the list and prints it
        # once it has been scrabbled
        word = random.choice(list_of_random_words)
        scrabbled_word = (turn_word_into_list(scrabble_word((word))))
        print(scrabbled_word)

        # Prompts the user for their first guess and also 
        # gives the the choice to get a new word or to stop
        # the program
        user_guess = input("What is your guess? Or type 1 for a different word. Or type '4' to stop.\n").lower()
        # Attempts begin to be tracked
        attempts = 1
        if user_guess == '4':
            print(f"You have guessed {correct_guesses} words correctly.")
            break
        # If the user guesses incorrectly, it lets asks them to guess
        # again but also gives them the choice to end the program
        while user_guess != word:
            if user_guess == "1":
                print(f"The correct word was '{word}'. Here is a new word: \n")

                break
            attempts += 1
            print(scrabbled_word)
            user_guess = input("Incorrect! What is your guess? Or type 1 for a different word. Or type '4' to stop.\n").lower()
            # If the user chooses to end the program, it 
            # will provide how many guesses were correct
            if user_guess == '4':
                print(f"You have guessed {correct_guesses} words correctly.")
                break
        
        # If user types '1', the program will give them a 
        # new word to guess
        if user_guess == "1":
            continue
        
        # If the user guesses correct, the number of guesses 
        # increases by 1 and prompts them to guess a new word
        if user_guess == word:
            correct_guesses += 1

        # Tells the user how many guesses it took to get the word right
        print(f"Correct! It took you {attempts} guess(es) to guess the word '{word}'.")

        # Asks the user if they want to continue,
        # If input is 'N' then the program ends and gives the 
        # correct number of words guessed
        user_input2 = input("Enter Y to continue or N to stop: ")
        if user_input2.upper() == "N":
            print(f"You have guessed {correct_guesses} words correctly.")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
