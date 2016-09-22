
import random
secret_number = random.randint(1, 10)
guesses = 5

while guesses == 5:
    while guesses > 0:
        print "Guess a number 1-10"
        yournumber = int(raw_input("your number:" ))
        guesses = guesses - 1
        print "you have %d guess(es) left" % guesses
        if yournumber == secret_number:
            print "Bingo, you win a brand new NADA 0.0"
            # global guesses
            guesses = -1
        elif yournumber < secret_number:
            print "lol too low. try again"
        elif yournumber > secret_number:
            print "lol too high. Try again"


    if guesses == 0:
        print "Unlucky bro"
    print "Do you wanna play again?"
    new_game = raw_input("Y/N: ")
    if new_game == "Y":
        guesses = 5
    if new_game == "N":
        print "fine bye"









# count = 0
# while count < 10:
#     print "Count is %d" % count
#     count = count + 1
# print "Done."
