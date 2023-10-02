from time import sleep
from datetime import datetime
import random
import os
import headings


def invalid():  # Function definition for invalid choice
    print('\033[1;31m' + 'You have entered an invalid choice!'+ '\033[0m')
    sleep(2)
    os.system('cls')


def admin_portal(choice):  # Function definition for admin portal
    if choice == 1:  # inputs new words in file
        new_words = input('\033[1;36m' + 'Please enter new word(s) separated by spaces: ' + '\033[0m').lower()
        with open('words.txt', 'a') as f:
            f.write(' ' + new_words.strip())
        print('New words entered successfully!')
        sleep(1.5)

    elif choice == 2:  # Resets the highscores
        ask = input('\033[1;31m' + 'Are you sure you want to reset all highscores? (Y/N) ' + '\033[0m').upper()
        if ask == 'Y':
            f2 = open('HighScore.txt', 'w')
            f2.close()
            print('\033[1;36m' + 'Highscores have been reset successfully!' + '\033[0m')
            sleep(2)

    else:
        invalid()


def file_search(player_name, player_points):
    # Function definition to save high scores in file
    lst = []
    # initializing list to store all the lines of the file
    with open('HighScore.txt', 'r+') as f:
        # opening file in read mode to save the contents of file in main memory
        for line in f:
            lst.append(line.split())

        with open('HighScore.txt', 'w') as f:
            # opening file in write mode to delete the current contents of the file

            if 1 <= len(lst) <= 3:
                # checking the previous records of the file

                for i in range(len(lst) if len(lst) <= 3 else 3):
                    # this loop checks if the current score outranks the previous scores

                    if player_points > int(lst[i][2]):
                        lst[i:i] = [
                            # if the points outdo any of the previous scores, the rank is changed
                            [str(i + 1), player_name, str(player_points), datetime.now().strftime("%d/%m/%Y"),
                             datetime.now().strftime("%H:%M:%S")]]
                        rank = i + 1
                        break
                else:
                    # if not, the new record is appended to the list of records
                    lst.append([str(i + 1), player_name, str(player_points), datetime.now().strftime("%d/%m/%Y"),
                                datetime.now().strftime("%H:%M:%S")])
                    rank = i + 2
                for i in range(len(lst) if len(lst) <= 3 else 3):
                    # the top 3 will now be written to the file
                    f.write(
                        f'{str(i + 1): ^10s} {lst[i][1]:^20s} {lst[i][2]:^10s} {lst[i][3] + " " + lst[i][4]:^20s}\n')

            else:  # if there is no data in list, put the record in the top rank
                f.write(
                    f'{str(1):^10s} {player_name:^20s} {str(player_points):^10s} {datetime.now().strftime("%d/%m/%Y %H:%M:%S"):^20s}\n')
                rank = 1

            if rank > 3:
                return None
            else:
                return rank


def main_game(name):  # Function definition for Main Game
    game_play = 'Y'

    while game_play == 'Y':
        os.system('cls')
        print('\033[1;35m' + f'Welcome to the Gallows, {name}\n' + '\033[0m')
        sleep(1.5)
        print(f'\033[1;36m' + "Loading words list from the file...." + '\033[0m')
        with open('words.txt') as f:  # Reading words from file(Loading to primary memory)
            word_list = f.read()
        word_list = word_list.split()  # converting the string data to list
        word = random.choice(word_list)  # selecting a random word from list
        sleep(1.5)
        print(word)
        display = '_'* len(word)
        guessed_letters = ''
        warning, t_guess = 3, 6
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z']
        print(f'{len(word_list)} words are loaded\n\nI have selected a\\an {len(word)} letters long word for you')
        sleep(1.5)
        while t_guess > 0 and display != word:
            if warning >= 0:
                print(f"\nYou have {t_guess} guesses and {warning} warnings left.\n")
            else:
                print(f"\nYou have {t_guess} guesses 0 warnings left.\n")

            print(f"\033[1;32mAvailable letters:\033[0m {''.join(letters)}\n\033[1;33mGuessed letters:\033[0m {guessed_letters}")
            print(display)
            print()
            guess = input('\033[1;36m' + "\nPlease guess a letter:" + '\033[0m').lower()
            os.system('cls')

            if guess not in letters:  # if guess is not in 'letters' and/or 'word'
                if len(guess) > 1:
                    print('\033[1;31m' + 'Please enter a single letter' + '\033[0m')
                elif not guess.isalpha():
                    print('\033[1;31m' + "That's  not a valid character, you fool!" + '\033[0m')
                elif guess in word:
                    print('\033[1;31m' + 'You have already guessed this letter, dumbo!' + '\033[0m')
                else:  # if guess is neither in 'word' nor in 'letters'
                    print('\033[1;31m' + 'You have already guessed this incorrect letter, dumbo!' + '\033[0m')
                warning -= 1
                if warning <= -1:
                    t_guess -= 1

            elif guess in word:  # if guess is in 'letters' and 'word'
                for i in range(len(word)):
                    if word[i] == guess:
                        display = display[:i] + guess + display[i + 1:]
                print('\033[1;32m' + 'Good Guess'+ '\033[0m')
                guessed_letters += guess
                letters.remove(guess)

            else:  # guess is in 'letters' but not in 'word'
                if guess in 'aeiou':
                    t_guess -= 2
                    print('\033[1;31m' + f"You guessed a vowel that was not in my word! Haha, I smell your death, {name}" + '\033[0m')
                elif guess in letters:
                    t_guess -= 1
                    print('\033[1;31m' + "That was never in my word, Fool!"+ '\033[0m')
                guessed_letters += guess
                letters.remove(guess)
            headings.hangman(t_guess)
            sleep(0.5)

        os.system('cls')
        if display == word:  # runs only if the player wins the game
            headings.win()
            word = set(word)
            dict = {1: 'First', 2: 'Second', 3: 'Third'}
            score = len(word) * t_guess
            highScore = file_search(name, score)
            if highScore is not None:
                print(f"How Incredible! You've made the {dict[highScore]} highest score!")
            print('Congratulations warrior! you indeed have a very noble heart and boundless knowledge!')
            print('\033[1;35m' +"""
                        _____
                        |/   
                        |
                        |   (v)
                        |   \|/
                        |    |
                        |   / \\
                        |---------
                        """+ '\033[0m')
            print('\033[1;33m' + f'\nScore reached: {score}' + '\033[0m')
        else:
            headings.lose()
            print('You will now be hanged! HAHAHAA')
            print('\033[1;31m' +
                """
                        ____
                        |/   |
                        |   (_)
                        |   /|\\
                        |    |
                        |   / \\
                        |
                        |_____
                        """ + '\033[0m')
            sleep(2)
            print('Hmm...Let\'s give you another shot, your points have been summoned though.\n')
        score = 0
        game_play = input('\033[1;36m' + 'Would you like to continue playing?(Y/N)' + '\033[0m').upper()
        sleep(2)
        os.system('cls')


headings.welcome()
while True:
    headings.menu()
    choice = int(input('Enter 1 to play a new game\nEnter 2 for Administrative Setup\nEnter 3 to '
                       'view High score \nEnter 4 to close the app\n\n\033[1;35mCHOICE: \033[0m'))  # Main menu interface
    sleep(1.5)

    if choice == 1:
        os.system('cls')
        print('\033[1;36m' + '\nOh Noble Warrior! Please enter thee\'s name!\n' + '\033[0m')
        name = input().split()[0]
        sleep(1.5)
        print('\033[1;3m' +  # A Dramatic opening of the game
              f'\n\tThis is the game in life!\n\tThe game everyone loves to play!\n\tUnfortunately, {name} is the fallen '
              f'victim\n\tI\'m scared you won\'t be able to maybe stay!\n\n\tEveryone seems to enjoy this game!\n\tIn smiles '
              f'they\'ve told you cruel things\n\tThey said that you deserved to die!\n\tAnd the tears in your eyes they '
              f'don\'t see!\n\n\tSo warrior, now tis your time\n\tThe time for {name} to wrong all of them\n\tHence, now you '
              f'should prepare to win\n\tAnd mark end to this terrible din!+ \033[0m\n\n\033[1;32mGood Luck\033[0m, {name}!')
        input('\033[1;36m' + 'Press enter to read the rules...' + '\033[0m')
        sleep(1.5)
        os.system('cls')
        print('\033[1;35m' + 'RULES\n' + '\033[0m')
        print(  # Rules
            f'\033[1;36mDear {name}!For this deathly trial, you have been given 6 guesses and 3 warnings \033[0m\n1. In case of '
            f'entering the wrong consonant, you will lose a guess.\n2. In case of using a special character, '
            f'digit or a used letter, you will lose a warning.\n3. In case of entering a wrong vowel, you will lose '
            f'two guesses.\n4. In case of running out of all warnings, your guesses will begin to subtract.\n5. If all '
            f'the guesses end, you will lose your life and all the points you collected throughout.\n'
            f'6. Your points will be kept in record if you win the game with a good high score.\n')
        input('\033[1;36m' + 'Press enter when ready for the trial...' + '\033[0m')
        main_game(name)

    elif choice == 2:  # Activating Administrator Block
        os.system('cls')

        while True:
            headings.admin()
            print('\033[1;35m' + '\nADMINISTRATOR LOGIN CREDENTIALS\n' + '\033[0m')
            username = input('\033[1;36mEnter username: \033[0m')
            password = input('\033[1;36mEnter password: \033[0m ')

            while username == 'NMAdev' and password == '*Code4Life*':
                os.system('cls')
                print('\nWelcome back master! What would you like to do?')
                choice = int(input('1. Enter 1 to add new words\n2. Enter 2 to reset highscores\n3. Enter 3 to return '
                                   'to the main menu\n\n\033[1;35mChoice: ' + '\033[0m'))
                if choice == 3:  # return to main menu
                    break
                admin_portal(choice)
            else:  # if the user enters invalid credentials
                print('\033[1;31mInvalid username and/or password\033[0m')
                if input(
                        '\033[1;36m' + 'Do you want to return to the main menu(Y/N)? ' + '\033[0m').upper() == 'Y':  # For unconcerned users
                    os.system('cls')
                    break
            sleep(1.5)
            os.system('cls')

            if choice == 3:  # to break entirely from the administrator loop
                break

    elif choice == 3:  # For viewing Highscores
        os.system('cls')
        with open('HighScore.txt') as f2:  # Opening high score file
            print('\033[1;33m' +f'{"Rank":^10s} {"Username":^20s} {"Score":^10s} {"Date/Time":^20s}\n'+ '\033[0m')
            for line in f2:
                print(line, end='')
            input('\033[1;36m' + '\nPress enter to return to the main menu...' + '\033[0m')
            os.system('cls')

    elif choice == 4:  # Terminates the entire program
        headings.bye()
        exit(0)

    else:
        invalid()
