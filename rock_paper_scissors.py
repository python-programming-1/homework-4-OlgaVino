import random
widgets = ['rock', 'scissors', 'paper']
win_score = 0
comp_score = 0
move = input("Make a move! (r/s/p)")


def play(guess):
    while True:
        global win_score
        global comp_score
        c_m = random.choice(widgets)  # computer move
        if guess == "r":
            guess = widgets[0]
        elif guess == "s":
            guess = widgets[1]
        elif guess == "p":
            guess = widgets[2]
        if (guess == 'rock' and c_m == 'scissors') or (guess == 'scissors' and c_m == 'paper') or (guess == 'paper' and c_m == 'rock'):
            win_score += 1
            print("You chose " + guess + " and the computer chose " + c_m + ". You win!")
        elif (guess == 'rock' and c_m == 'paper') or (guess == 'scissors' and c_m == 'rock') or (guess == 'paper' and c_m == 'scissors'):
            comp_score += 1
            print("You chose " + guess + " and the computer chose " + c_m + ". You lose!")
        elif guess == c_m:
            print("You chose " + guess + " and the computer chose " + c_m + ". Draw! Try again!")
        elif guess == "sc":
            print("human: " + str(win_score) + ", computer: " + str(comp_score))
        reply = input("Do you want to play again? (y/n)")
        if reply == "y":
            print("Make a move! (r/s/p)")
            new_move = input()
            play(new_move)
        if reply == "n":
            print("Thanks bye!")
        break


play(move)
