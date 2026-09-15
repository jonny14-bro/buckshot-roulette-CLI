#  Buckshot Roullete
'''

- It will be a single player game , will also cover the
  all the basic python fundamentals as well help you to 
  build logics as well connecting different funtions .

- you will get a clear idea that how a data is processed 
  with carrying logic of the program means you will know
  how a pipeline in a program is made to process

- It will be a simple CLI based UI program like this 

    ================================
            BUCKSHOT ROULETTE
    ================================

    < ASCII UI FOR BETTER VISUALS >

    Your Health: 3 ❤️
    Dealer Health: 3 ❤️

    Shotgun:
    [ ?, ?, ?, ? ]

    Shells: 4
    Live: 2
    Blank: 2

    Your turn!

    1. Shoot yourself
    2. Shoot dealer

    Enter choice:

'''

import random


def ascii(selection):

    ascii_1 = '''

████  █   █  ███  █   █  ████ █   █  ███  █████    ████   ███  █   █ █     █████ █████ █████ █████   
█░░░█ █░  █░█ ░░░ █░ █ ░█ ░░░░█░  █░█ ░░█  ░█░░░   █░░░█ █ ░░█ █░  █░█░    █░░░░░ ░█░░░ ░█░░░█░░░░░  
████░░█░░ █░█░ ░░░███ ░ ░███░░█████░█░ ░█░  █░░░░  ████░░█░ ░█░█░░ █░█░░   ████░░░ █░░░░ █░░░████░░░ 
█░░░█ █░░ █░█░░   █░░█ ░  ░░█ █░░░█░█░░ █░░ █░░    █░░█░ █░░ █░█░░ █░█░░   █░░░░   █░░   █░░ █░░░░   
████░░ ███ ░░███  █░░░█ ████░░█░░░█░░███ ░░ █░░    █░░░█░ ███ ░░███ ░█████ █████░  █░░   █░░ █████░  
 ░░░░ ░ ░░░ ░ ░░░  ░░  ░ ░░░░ ░░░  ░░ ░░░ ░  ░░     ░░  ░  ░░░ ░ ░░░ ░░░░░░ ░░░░░   ░░    ░░  ░░░░░  
  ░░░░   ░░░   ░░░  ░   ░ ░░░░  ░   ░  ░░░    ░      ░   ░  ░░░   ░░░  ░░░░░ ░░░░░   ░     ░   ░░░░░ 
'''

    ascii_2 = '''

####  #   #  ###  #   #  #### #   #  ###  #####    ####   ###  #   # #     ##### ##### ##### #####   
#░░░# #░  #░# ░░░ #░ # ░# ░░░░#░  #░# ░░#  ░#░░░   #░░░# # ░░# #░  #░#░    #░░░░░ ░#░░░ ░#░░░#░░░░░  
####░░#░░ #░#░ ░░░### ░ ░###░░#####░#░ ░#░  #░░░░  ####░░#░ ░#░#░░ #░#░░   ####░░░ #░░░░ #░░░####░░░ 
#░░░# #░░ #░#░░   #░░# ░  ░░# #░░░#░#░░ #░░ #░░    #░░#░ #░░ #░#░░ #░#░░   #░░░░   #░░   #░░ #░░░░   
####░░ ### ░░###  #░░░# ####░░#░░░#░░### ░░ #░░    #░░░#░ ### ░░### ░##### #####░  #░░   #░░ #####░  
 ░░░░ ░ ░░░ ░ ░░░  ░░  ░ ░░░░ ░░░  ░░ ░░░ ░  ░░     ░░  ░  ░░░ ░ ░░░ ░░░░░░ ░░░░░   ░░    ░░  ░░░░░  
  ░░░░   ░░░   ░░░  ░   ░ ░░░░  ░   ░  ░░░    ░      ░   ░  ░░░   ░░░  ░░░░░ ░░░░░   ░     ░   ░░░░░ 

'''

    ascii_3 = '''

****  *   *  ***  *   *  **** *   *  ***  *****    ****   ***  *   * *     ***** ***** ***** ***** 
*   * *   * *     *  *  *     *   * *   *   *      *   * *   * *   * *     *       *     *   *     
****  *   * *     ***    ***  ***** *   *   *      ****  *   * *   * *     ****    *     *   ****  
*   * *   * *     *  *      * *   * *   *   *      *  *  *   * *   * *     *       *     *   *     
****   ***   ***  *   * ****  *   *  ***    *      *   *  ***   ***  ***** *****   *     *   ***** 

'''

    ascii_4 = '''

@@@@  @   @  @@@  @   @  @@@@ @   @  @@@  @@@@@    @@@@   @@@  @   @ @     @@@@@ @@@@@ @@@@@ @@@@@   
@░░░@ @░  @░@ ░░░ @░ @ ░@ ░░░░@░  @░@ ░░@  ░@░░░   @░░░@ @ ░░@ @░  @░@░    @░░░░░ ░@░░░ ░@░░░@░░░░░  
@@@@░░@░░ @░@░ ░░░@@@ ░ ░@@@░░@@@@@░@░ ░@░  @░░░░  @@@@░░@░ ░@░@░░ @░@░░   @@@@░░░ @░░░░ @░░░@@@@░░░ 
@░░░@ @░░ @░@░░   @░░@ ░  ░░@ @░░░@░@░░ @░░ @░░    @░░@░ @░░ @░@░░ @░@░░   @░░░░   @░░   @░░ @░░░░   
@@@@░░ @@@ ░░@@@  @░░░@ @@@@░░@░░░@░░@@@ ░░ @░░    @░░░@░ @@@ ░░@@@ ░@@@@@ @@@@@░  @░░   @░░ @@@@@░  
 ░░░░ ░ ░░░ ░ ░░░  ░░  ░ ░░░░ ░░░  ░░ ░░░ ░  ░░     ░░  ░  ░░░ ░ ░░░ ░░░░░░ ░░░░░   ░░    ░░  ░░░░░  
  ░░░░   ░░░   ░░░  ░   ░ ░░░░  ░   ░  ░░░    ░      ░   ░  ░░░   ░░░  ░░░░░ ░░░░░   ░     ░   ░░░░░ 

'''

    ascii_5 = '''

    @@@@  @   @  @@@  @   @  @@@@ @   @  @@@  @@@@@    @@@@   @@@  @   @ @     @@@@@ @@@@@ @@@@@ @@@@@ 
   @   @ @   @ @     @  @  @     @   @ @   @   @      @   @ @   @ @   @ @     @       @     @   @      
  @@@@  @   @ @     @@@    @@@  @@@@@ @   @   @      @@@@  @   @ @   @ @     @@@@    @     @   @@@@    
 @   @ @   @ @     @  @      @ @   @ @   @   @      @  @  @   @ @   @ @     @       @     @   @        
@@@@   @@@   @@@  @   @ @@@@  @   @  @@@    @      @   @  @@@   @@@  @@@@@ @@@@@   @     @   @@@@@     

'''

    if selection == 1:
        return ascii_1

    elif selection == 2:
        return ascii_2

    elif selection == 3:
        return ascii_3

    elif selection == 4:
        return ascii_4

    elif selection == 5:
        return ascii_5

    else:
        return " ---- INVALID INPUT ---- "


def engine():

    user_round_wins = 0
    dealer_round_wins = 0

    round_no = 1

    while round_no <= 3:

        if round_no == 1:

            dealer_lives = 6
            user_health = 6

            loaded_stat = load_magazine(round_no)

            live_round = loaded_stat.count("LIVE")
            blank_round = loaded_stat.count("BLANK")

            while len(loaded_stat) != 0 and dealer_lives != 0 and user_health != 0:

                ui(
                    round_no,
                    dealer_lives,
                    user_health,
                    loaded_stat,
                    live_round,
                    blank_round
                )

                print(" 1. Shoot Dealer")
                print(" 2. Shoot Yourself")

                try:
                    choice = int(input("Enter the choice:  "))
                except ValueError:
                    print("\n ---- Please enter a valid number ---- \n")
                    continue

                match choice:

                    case 1:

                        if loaded_stat[-1] == "LIVE":

                            response = " BANG ! You shot the Dealer "

                            dealer_lives -= 1
                            loaded_stat.pop()
                            live_round -= 1

                        else:

                            response = " Pussss ! The shot was Blank "

                            loaded_stat.pop()
                            blank_round -= 1

                    case 2:

                        if loaded_stat[-1] == "LIVE":

                            response = " BANG ! You shot Yourself "

                            user_health -= 1
                            loaded_stat.pop()
                            live_round -= 1

                        else:

                            response = " Pussss ! The shot was Blank, you are safe .... "

                            loaded_stat.pop()
                            blank_round -= 1

                    case _:

                        response = " ---- Invalid Choice ---- "

                print(f"\n <-- {response} --> \n")

            if dealer_lives == 0:
                user_round_wins += 1
                winner_ui("USER", round_no, dealer_lives, user_health)

            elif user_health == 0:
                dealer_round_wins += 1
                winner_ui("DEALER", round_no, dealer_lives, user_health)

            else:
                winner_ui("DRAW", round_no, dealer_lives, user_health)


        elif round_no == 2:

            dealer_lives = 5
            user_health = 5

            loaded_stat = load_magazine(round_no)

            live_round = loaded_stat.count("LIVE")
            blank_round = loaded_stat.count("BLANK")

            while len(loaded_stat) != 0 and dealer_lives != 0 and user_health != 0:

                ui(
                    round_no,
                    dealer_lives,
                    user_health,
                    loaded_stat,
                    live_round,
                    blank_round
                )

                print(" 1. Shoot Dealer")
                print(" 2. Shoot Yourself")

                try:
                    choice = int(input("Enter the choice:  "))
                except ValueError:
                    print("\n ---- Please enter a valid number ---- \n")
                    continue

                match choice:

                    case 1:

                        if loaded_stat[-1] == "LIVE":

                            response = " BANG ! You shot the Dealer "

                            dealer_lives -= 1
                            loaded_stat.pop()
                            live_round -= 1

                        else:

                            response = " Pussss ! The shot was Blank "

                            loaded_stat.pop()
                            blank_round -= 1

                    case 2:

                        if loaded_stat[-1] == "LIVE":

                            response = " BANG ! You shot Yourself "

                            user_health -= 1
                            loaded_stat.pop()
                            live_round -= 1

                        else:

                            response = " Pussss ! The shot was Blank, you are safe .... "

                            loaded_stat.pop()
                            blank_round -= 1

                    case _:

                        response = " ---- Invalid Choice ---- "

                print(f"\n <-- {response} --> \n")

            if dealer_lives == 0:
                user_round_wins += 1
                winner_ui("USER", round_no, dealer_lives, user_health)

            elif user_health == 0:
                dealer_round_wins += 1
                winner_ui("DEALER", round_no, dealer_lives, user_health)

            else:
                winner_ui("DRAW", round_no, dealer_lives, user_health)


        elif round_no == 3:

            dealer_lives = 3
            user_health = 3

            loaded_stat = load_magazine(round_no)

            live_round = loaded_stat.count("LIVE")
            blank_round = loaded_stat.count("BLANK")

            while len(loaded_stat) != 0 and dealer_lives != 0 and user_health != 0:

                ui(
                    round_no,
                    dealer_lives,
                    user_health,
                    loaded_stat,
                    live_round,
                    blank_round
                )

                print(" 1. Shoot Dealer")
                print(" 2. Shoot Yourself")

                try:
                    choice = int(input("Enter the choice:  "))
                except ValueError:
                    print("\n ---- Please enter a valid number ---- \n")
                    continue

                match choice:

                    case 1:

                        if loaded_stat[-1] == "LIVE":

                            response = " BANG ! You shot the Dealer "

                            dealer_lives -= 1
                            loaded_stat.pop()
                            live_round -= 1

                        else:

                            response = " Pussss ! The shot was Blank "

                            loaded_stat.pop()
                            blank_round -= 1

                    case 2:

                        if loaded_stat[-1] == "LIVE":

                            response = " BANG ! You shot Yourself "

                            user_health -= 1
                            loaded_stat.pop()
                            live_round -= 1

                        else:

                            response = " Pussss ! The shot was Blank, you are safe .... "

                            loaded_stat.pop()
                            blank_round -= 1

                    case _:

                        response = " ---- Invalid Choice ---- "

                print(f"\n <-- {response} --> \n")

            if dealer_lives == 0:
                user_round_wins += 1
                winner_ui("USER", round_no, dealer_lives, user_health)

            elif user_health == 0:
                dealer_round_wins += 1
                winner_ui("DEALER", round_no, dealer_lives, user_health)

            else:
                winner_ui("DRAW", round_no, dealer_lives, user_health)

            final_winner_ui(user_round_wins, dealer_round_wins)


        round_no += 1

    return round_no


def load_magazine(round_no):

    max_shells = min(2 + round_no, 8)

    min_shells = max(3, max_shells - 1)

    total_shells = random.randint(min_shells, max_shells)

    live_shells = random.randint(1, total_shells - 1)

    blank_shells = total_shells - live_shells

    magazine = (
        ["LIVE"] * live_shells +
        ["BLANK"] * blank_shells
    )

    random.shuffle(magazine)

    return magazine


def ui(
    round_no,
    dealer_health,
    user_health,
    loaded_stat,
    live_shells,
    blank_shells
):

    print("===========================================")
    print("      <***    BUCKSHOT ROULETTE   ***>     ")
    print("===========================================")

    print(f" --- ROUND : {round_no} ")

    print(" **** HEALTH SECTION **** \n")
    print(f" DEALER : {dealer_health} ❤️")
    print(f" USER : {user_health} ❤️")
    print(f" Shells loaded {loaded_stat} \n\n")

    print(" *** stat of game *** \n")
    print(f" LIVE SHELLS : {live_shells}")
    print(f" BLANK SHELLS : {blank_shells}")
    print(f" Total shels present : {len(loaded_stat)}")



def final_winner_ui(user_round_wins, dealer_round_wins):

    print("\n")
    print("===========================================")

    if user_round_wins > dealer_round_wins:

        print("          👑  GAME OVER — YOU WIN !  👑")
        print("-------------------------------------------")
        print()
        print("              FINAL RESULT")
        print()
        print(f"        YOU    : {user_round_wins} ROUND WINS")
        print(f"        DEALER : {dealer_round_wins} ROUND WINS")
        print()
        print("           CONGRATULATIONS!")

    elif dealer_round_wins > user_round_wins:

        print("          💀  GAME OVER — DEALER WINS !  💀")
        print("-------------------------------------------")
        print()
        print("              FINAL RESULT")
        print()
        print(f"        YOU    : {user_round_wins} ROUND WINS")
        print(f"        DEALER : {dealer_round_wins} ROUND WINS")
        print()
        print("             BETTER LUCK!")

    else:

        print("          🤝  GAME OVER — DRAW !  🤝")
        print("-------------------------------------------")
        print()
        print("              FINAL RESULT")
        print()
        print(f"        YOU    : {user_round_wins} ROUND WINS")
        print(f"        DEALER : {dealer_round_wins} ROUND WINS")
        print()
        print("            PERFECT TIE!")

    print("===========================================\n")



def winner_ui(winner, round_no, dealer_health, user_health):

    print("\n")
    print("===========================================")

    if winner == "USER":

        print(f"          🏆  ROUND {round_no} WINNER  🏆")
        print("-------------------------------------------")
        print()
        print("        The Dealer is DOWN !")
        print()
        print(f"        DEALER : {dealer_health} ❤️")
        print(f"        USER   : {user_health} ❤️")

    elif winner == "DEALER":

        print(f"          💀  ROUND {round_no} WINNER  💀")
        print("-------------------------------------------")
        print()
        print("        You have been defeated !")
        print()
        print(f"        DEALER : {dealer_health} ❤️")
        print(f"        USER   : {user_health} ❤️")

    else:

        print("          🤝  ROUND DRAW !  🤝")
        print("-------------------------------------------")
        print()
        print("        No shells remaining !")
        print()
        print(f"        DEALER : {dealer_health} ❤️")
        print(f"        USER   : {user_health} ❤️")

    print("===========================================\n")



if __name__ == "__main__":

    ui_selection = random.randint(1, 5)

    print(ascii(ui_selection))

    engine()