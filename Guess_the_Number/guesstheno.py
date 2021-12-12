import playsound
import random
"""Use of Binary Search"""
no=random.randint(1,99)
guesses=10
print('\n')
print("\t\t-------------------------------------------------")
print('\t\t|\tWelcome to Guessing the Number Game\t|')
print('\t\t|\t\t\t\t\t\t|')
print('\t\t|\t        Total {} chances\t\t|'.format(guesses))
print("\t\t-------------------------------------------------")
print("\nLet's start by now....start guessing the number :-\n")
print("Hint: Number is less then 100 :-\n")

def howmuch(number,guess):
    if number > guess:
        difference = number - guess
    else:
        difference = guess - number
    return difference

def winning_music():
    """play winning music"""
    win_music  =["Sound_tracks/anime_wow.mp3","Sound_tracks/smb_world_clear.mp3"]
    try:
        playsound.playsound(random.choice(win_music),True)
    except Exception as e:
        print(e)    

def losing_music():
    """play losing music"""
    lose_music = ["Sound_tracks/Nope.mp3","Sound_tracks/smb_gameover.mp3"]
    try:
        playsound.playsound(random.choice(lose_music),True)
    except Exception as e:
        print(e)   

if __name__ == '__main__':
    """initial no of guesses are zero"""
    chances = 0
    while chances < guesses:
        try:
            guess_num  = int(input("Guess The Number: "))
            """incrementing number of chances after taking input"""
            chances += 1 
        except :
            print('\nPlease enter a number....\n')
            continue
    
        if guess_num < no:
            if howmuch(no,guess_num) <= 5:
                print(f"\nStill smaller, But you are closer to the actual number..keep guessing Good luck! chances left:{guesses-chances}\n")
    
            elif howmuch(no,guess_num) >5 and howmuch(no,guess_num) <=10:
                print(f"\nBit Smaller, But you are on a right path....keep guessing. chances left:{guesses-chances}\n")

            else:
                print(f'\nNooo....Guessed Number is less than actual number! Try to get closer.... chances left:{guesses-chances}\n')

        elif guess_num > no:
            if howmuch(no,guess_num) <=5:
                print(f"\nStill Higher, But you are closer to the actual number..keep guessing Good luck! chances left:{guesses-chances}\n")
    
            elif howmuch(no,guess_num) > 5 and howmuch(no,guess_num) <=10:
                print(f"\nBit Higher, But you are on a right path....keep guessing. chances left:{guesses-chances}\n")

            else:
                print(f'\nNooo....Guessed Number is greater than actual number! Try to get closer.... chances left:{guesses-chances}\n')

        else:
            print(f"\nWoooohoooh....WINNER.... congratulations You took {chances} chances.\n")
            winning_music()
            exit(1)

        if chances == guesses:
            print("Out of chances!\n")
            print("You are not smarter than me see yaa.....\n")
            print('----------------Game Over---------------\n')
            losing_music()
            exit(1)

    





