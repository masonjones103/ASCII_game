''' Hello, this is the starting code for my WIP ASCII game.

#TO-DO:
 - FIX: Occasional Out-Of-Bounds Error(?)
 - Add new equipment
 - Make movement one button press
 - Make separate file for ASCII art
 - Add color in terminal
 - Fix tutorial
#DOING:
 - Fixing combat dialogue positioning
#DONE:
 - Added bounds to the room
 - Added collision to enemy
 - Made goblin in ASCII
 - Fix combat so that goblin does not change attacks when the player inputs the wrong value
 - Adding combat
 - Add treasure room
 - Print different goblins based on enemy health
 - Add further combat dialogue
 - Add health and energy bar to combat screen
 - Adding a game over screen for when the player dies
'''

import os
import random

# stores the row and index of the player character. [4, 3] is the starting position of the '@' character.
position = [4, 3]

# stores the symbol the player walks over so it can be returned after they walk off.
stored_char = [4, 3, ' ']

# room stored as nested lists
room1 = [
         ['[', '=', '=', '-', '=', '=', ']'],
         ['[', ' ', ' ', 'g', ' ', '~', ']'],
         ['[', '~', ' ', ' ', ' ', ' ', ']'],
         ['[', ' ', ' ', ' ', ' ', '~', ']'],
         ['[', '~', ' ', ' ', ' ', ' ', ']'],
         ['[', '=', '=', '-', '=', '=', ']'],
         ]

# sets list values where the player cannot step on, the walls.
bounds = [
    [[0, 0], [0, 1], [0, 2],         [0, 4], [0, 5], [0, 6],],
    [[1, 0],                                         [1, 6],],
    [[2, 0],                                         [2, 6],],
    [[3, 0],                                         [3, 6],],
    [[4, 0],                                         [4, 6],],
    [[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6]]
]

# a very scary goblin. Added wounded versions that appear when various health thresholds are crossed.
goblin1 = r'''
                            /\     /\
                           (  \___/  )
                            |       |
                            \ o' 'o /
                             | """ |     __
                     ^^      \ """ /     \_\
                     \ \      |   |      /  |_ 
                      \ \____/     \____/ /\  |>
                       \_____ .   . _____/  \  |>
                            /       \        \  |>
                           /    .    \        \/
                          {----(#)----}      
                          {           }
                          {_/\_____/\_}
                            ||     ||
                            (|     |)
                            ||     ||
                           /  \   /  \
                           ^^^^   ^^^^
'''

goblin_wounded1 = r'''   
                            /\     /\
                           (  \___/  )
                            |       |
                            \ o' 'o /
                             | """ |     __
                             \ """ /     \_\
                              |   |      /  |_
                         ____/     \____/ /\  |>
                        | ___ .   . _____/  \  |>
                        | | /       \        \  |>
                        \ >)    .    \        \/
                        ~ {----(#)----}        
                        ~ {           }
                       ~~ {_/\_____/\_}
                       ~    ||     ||
                       ~    (|     |)
                       ~    ||     ||
                       ~   /  \   /  \
                     ~~~~~ ^^^^   ^^^^		
'''

goblin_wounded2 = r'''
                     	     /\
                     	    (  \___/**~
                            |       |~
                            \ o' 'o /~
                             | """ | ~   __
                             \ """ /     \_\
                              |   |      /  |_ 
                         ____/     \____/ /\  |>
                        | ___ .   . _____/  \  |>
                        | | /       \        \  |>
                        \ >)    .    \        \/
                        ~ {----(#)----}        
                        ~ {           }
                       ~~ {_/\_____/\_}
                       ~    ||     ||
                       ~    (|     |)
                       ~    ||     ||
                       ~   /  \   /  \
                     ~~~~~ ^^^^   ^^**~~~~~	
'''

goblin_wounded3 = r'''
                     	     /\ 
                     	    (  \___/**~
                            |       |~
                            \ o' '# /~
                             | """ | ~
                             \ """ /
                              |   |
                         ____/     \___
                        | ___ .   . __ \ __
                        | | /       \ \ \\_\
                        \ >)    . {} \ \___ |_
                        ~ {----(#)~~--}    \  |>
                        ~ {       ~   }     \  |>
                       ~  {_/\____~/\_}      \  |>
                       ~    ||    ~||         \/
                       ~    (|   ~ |)          ~
                       ~    ||   ~ ||          ~
                       ~   /  \  ~/  \         ~
                     ~~~~~~^^^^~~~^^**~~~~~  ~~~~~
'''

goblin_meet = r'''
            You meet face to face with the ferocious goblin.
              Will you (A)ttack the goblin or (R)un away?
'''

# screen appears when the player kills the goblin
goblin_dead = r'''






                                  ____
                              ___/   /
                             /     x |
                         ~~##| d   x \
                      ~~~~~~~~~~~~~~~~~~~~

Your swing connects with the goblin's neck and his head goes flying, decapitated.
'''

# treasure room displayed when the player defeats the goblin and enters the room behind him
treasure_room = r'''
 _______________________________________________________________________
|               |     ~~      | ~~~~~~~~~~ |   ~~       |               |
|               |       ~     |  ~~~~~~~~  |     ~      |               |
|               |      [#]    |   ~~~~~~   |    [#]     |               |
|               |       V     |  ~~~~~~~~  |     V      |               |
|               |             |     ~~     |            |               |
|               |             ^v^v^v^^v^v^v^            |               |
|               |                                    .  |               |
|               |                   ()           0  <|> |               |
|               |  ___________    _{++}_          \__|_ |               |
|               |_[-----#-----]___\----/__________(----)|               |
|              /  [___________]   /____\          (----) \              |
|             /                                           \             |
|            /                                             \            |
|         /|/                 ______________                \           |
|        / |                ~/ ------------ \~           __I_\          |
|       |  |_____          ~/ /            \ \~         |\(~)I\         |
|       | /*0* */|        ~/ /              \ \~        | \ (~)\        |
|       |/ *0 0/ /       ~/ /                \ \~       \  \____\       |
|      /|_*0_*/ /       ~/ /                  \ \~       \ |    |\      |
|     / |_____|/       ~/ /                    \ \~       \|____| \     |
|    / 0 * *          ~/ /                      \ \~               \    |
|   /     0          ~/ /                        \ \~               \   |
|  /                ~/ /                          \ \~               \  |
| /                ~/ /                            \ \~               \ |
|/                ~/ /                              \ \~               \|
'''

# game over screen
game_over = r'''
               ____       ____			       
               \   \     /   /   _______      __     ~~_
                \   \   /   /   /       \    |  |   ~|  |
                 \   \_/   /   /   ___   \   |  |   ~|  |
                  \_     _/   |   |   |   |  |  |   ~|  |
                    |   |     |   |___|   |  |  |~~~~|  |
                    |   |      ~         /   |  \~~~~/  |
                    |~__|      ~\_______/     \________/ 
                     ~         ~
                 _____~      _~~~___    ______     ______
                |  __  \~   |__~  __|  |  ____|   |  __  \
                | |  \  \~     | |     | |        | |  \  \
                | |   \  \~    | |     | |~~~~    | |   \  \
                | |    |  |~   | |     |  ___|~   | |    |  |
                | |___/  / ~ __| |__   | |_____~  | |___/  /
                |~~_____/  ~|_______|  |_______|~ |_______/
                 ~~        ~                    ~
                 ~         ~                    ~
                 ~         ~                    ~
            ~~~~~~~~~~~~~~~~~~~~~~~        ~~~~~~~~~~~~~~
'''

# the player's stat values
player_hp = 10
player_eg = 10

# the enemy's stat values
enemy_hp = 10
enemy_eg = 10

# set to False if the goblin dies
enemy_alive = True

# stores lines that happen upon certain conditions
lines = ['']

# prints a menu where the player can select to play or exit the game. Tutorial currently has a bug, so I have commented it out until I can figure out what is going wrong.
def menu():
    print('>----------<')
    print('(P)lay')
    # print('(T)utorial')
    print('(E)xit')
    print('>----------<')
    play = False
    exit_menu = False
    while play == False and exit_menu == False:
        menu_choice = input('>').lower().strip()
        if menu_choice == 'p':
            play = True
#         elif menu_choice == 't':
#             clear_screen()
#             pause = input('''
# Use WASD to move and Enter to confirm your choice.
# When you encounter an enemy, choose your combat style depending upon what the enemy is doing.
# Your health and energy are displayed on the screen.
# Certain attacks will lower your energy, don't let your energy hit 0!
# (Press enter to return to the menu...)
# >''')
#             clear_screen()
#             menu()
        elif menu_choice == 'e':
            exit_menu = True
        else:
            print('Please type (P) to play or (E) to exit.')
    if play:
        clear_screen()
        print('''Welcome to the Dungeon of Doom...
You enter a damp, musty room, water drips from the ceiling and torches set upon its walls grant a flicking light.
You see a shape looming in the distance, a menacing goblin with a vicious cleaver guards the far door.
You grasp your sword and move forward cautiously...''')
    elif exit_menu:
        quit()

# prints stat menu, uses .ljust to keep boundaries even regardless of variable length
def stats():
    print('[====================]')
    print(f'[ Health = {player_hp} '.ljust(21, ' '), end='')
    print(']')
    print(f'[ Energy = {player_eg} '.ljust(21, ' '), end='')
    print(']')
    print('[====================]')
    print('''
''')

# takes the room number, then prints each character in a row, iterates to the next row, and continues until all rows are printed.
def print_room(room):
    for row in room:
        print('')
        for char in row:
            print(char, end='')
    print('''
    ''')

# checks if the player is trying to move onto a boundary, if they are, it returns True
def check_bounds(boundaries, try_move):
        for row in boundaries:
            for char in row:
                if try_move == char:    #if the player is trying to move onto a wall
                    return True

# takes the room, row, and index numbers and changes the given spot to the char.
def change_char(room, row, index, char):
    value = True
    while value:
        room[row][index] = char
        value = False

# stored in lines if you encounter the goblin
def on_enemy():
    lines[0] = 'You meet face to face with the ferocious goblin.'

# prints stored lines, then clears the lines list.
def print_lines(lines):
    for line in lines:
        print(line)
        print('')
    lines[0] = ''

# updates the position list to give coordinates that your character will move to when update_char() is called. Very messy right now, I should clean it up and make more functions.
def move_char():
    new_position = [4, 3]   # where the player is trying to move, does not actually move there unless check_bound() returns False
    previous_position = [4, 3]  # where the player was standing before checking if a wall was in the way.
    previous_position[0] = position[0]
    previous_position[1] = position [1]
    move_input = input('''Press 'W' to move forward, 'S' to move back, 'A' to move left, or 'D' to move right.
Press enter to confirm your movement.
>''').upper().strip()
    if move_input == 'W':
        new_position[0] = position[0] - 1
        new_position[1] = position[1]
        if check_bounds(bounds, new_position):  # if there is a wall in the way, position is set to your previous position and a line is printed.
            lines[0] = '''You walk into the wall... ouch.'''
            position[0] = previous_position[0]
            position[1] = previous_position[1]
        elif new_position == [1, 3] and enemy_alive:    # if you walk into the enemy, text you won't move and text will appear.
            position[0] = previous_position[0]
            position[1] = previous_position[1]
            enemy_encounter()
        else:     # if there is no wall in the way, your move goes through and position is updated.
            position[0] = new_position[0]
    elif move_input == 'S':
        new_position[0] = position[0] + 1
        new_position[1] = position[1]
        if check_bounds(bounds, new_position):
            if new_position == [5, 3]:
                lines[0] = 'There is no escape, the solid stone door behind you has been locked by some hidden mechanism.'
            else:
                lines[0] = '''You walk into the wall... ouch.'''
                position[0] = previous_position[0]
                position[1] = previous_position[1]
        elif new_position == [1, 3] and enemy_alive:
            position[0] = previous_position[0]
            position[1] = previous_position[1]
            enemy_encounter()
        else:
            position[0] = position[0] + 1
    elif move_input == 'A':
        new_position[0] = position[0]
        new_position[1] = position[1] -1
        if check_bounds(bounds, new_position):
            lines[0] = '''You walk into the wall... ouch.'''
            position[0] = previous_position[0]
            position[1] = previous_position[1]
        elif new_position == [1, 3] and enemy_alive:
            position[0] = previous_position[0]
            position[1] = previous_position[1]
            enemy_encounter()
        else:
            position[1] = position[1] -1
    elif move_input == 'D':
        new_position[0] = position[0]
        new_position[1] = position[1] + 1
        if check_bounds(bounds, new_position):
            lines[0] = '''You walk into the wall... ouch.'''
            position[0] = previous_position[0]
            position[1] = previous_position[1]
        elif new_position == [1, 3] and enemy_alive:
            position[0] = previous_position[0]
            position[1] = previous_position[1]
            enemy_encounter()
        else:
            position[1] = position[1] + 1
    else:
        move_char()

# adds your character symbol to the list based on your position
def update_char(room):
    row = position[0]
    char = position[1]
    stored_char[0] = position[0]
    stored_char[1] = position[1]
    stored_char[2] = room[row][char]
    room[row][char] = '@'

# stores the symbol that will be covered by the player's symbol
def return_stored(room):
    row = stored_char[0]
    char = stored_char[1]
    symbol = stored_char[2]
    room[row][char] = symbol

# this function was copied from https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python it clears the terminal screen.
def clear_screen():
    """Clears the terminal screen."""

    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

# rolls from 1 - 3 and returns that number
def rand_1_3():
    x = random.randint(1, 3)
    return x

# if you encounter the goblin, this function clears the screen and prints the scary goblin
def enemy_encounter():
    clear_screen()
    print(goblin1)
    print(goblin_meet)
    choice1 = input('>').upper().strip()
    if choice1 == 'A':
        attack = input("You inch towards the goblin with your sword drawn and ready yourself for combat.")
        while player_hp > 0 or enemy_hp > 0:
            combat()
        pause = input('')
    elif choice1 == 'R':
        pause = input("You turn around to run, the goblin lunges onto your back and stabs you repeatedly until you die.")
        clear_screen()
        print(game_over)
        pause = input('')
        quit()
    else:
        enemy_encounter()

# determines the enemy's stance based of a random dice roll from 1-3.
def enemy_stance():
    rand_stance = random.randint(1, 3)
    if rand_stance == 1:
        stance = 'lightattack'
        return stance
    elif rand_stance == 2:
        stance = 'heavyattack'
        return stance
    elif rand_stance == 3:
        stance = 'parry'
        return stance

# gets the player's combat choice input
def player_stance():
    combat_choice = input('>').upper().strip()
    if combat_choice == 'L':
        x = 'L'
        return x
    elif combat_choice == 'H':
        x = 'H'
        return x
    elif combat_choice == 'P':
        x = 'P'
        return x

# runs through combat. I need to clean it up and split it into more functions probably.
def combat():
    enemy_l_atk = False
    enemy_h_atk = False
    enemy_p = False
    player_l_atk = False
    player_h_atk = False
    player_p = False

    global player_hp
    global player_eg
    global enemy_hp
    global enemy_eg

    clear_screen()
    # when the goblin's HP reaches certain thresholds different wounded goblins are printed.
    if enemy_hp > 7:
        print(goblin1)
    elif enemy_hp >= 5:
        print(goblin_wounded1)
    elif enemy_hp >= 3:
        print(goblin_wounded2)
    elif enemy_hp >= 1:
        print(goblin_wounded3)
    # gets the enemy's combat choice
    stance = enemy_stance()
    # prints the enemy's attack choice
    if stance == 'lightattack':
        rand_num = rand_1_3()
        if rand_num == 1:
            print('''
The goblin looks eager to dart in and prances lightly on his feet.''')
        elif rand_num == 2:
            print('''
The goblin juggles his cleaver between his hands and eyes you. It looks like he's gauging you.''')
        elif rand_num == 3:
            print('''
The goblin cackles maniacally and darts in and out, trying to fake you out.''')
        enemy_l_atk = True
    elif stance == 'heavyattack':
        rand_num = rand_1_3()
        if rand_num == 1:
            print('''
The goblin glares at you and growls menacingly before shifting his cleaver to hold it with two hands.''')
        elif rand_num == 2:
            print('''
The goblin howls at the ceiling, the frightful call echoes throughout the room
and his red eyes glitter at you menacingly. His muscles are taut with anticipation.''')
        elif rand_num == 3:
            print('''
The goblin grins at you, needle-like teeth glinting in the torch light. 
    He holds his cleaver high above his head and creeps forward slowly, 
        like a tiger stalking its prey before it lunges.''')
        enemy_h_atk = True
    elif stance == 'parry':
        rand_num = rand_1_3()
        if rand_num == 1:
            print('''
The goblin hisses at you and takes a step back, cleaver held up in front of its body.''')
        elif rand_num == 2:
            print('''
The goblin eyes you warily and braces itself as if expecting an attack.''')
        elif rand_num == 3:
            print('''
The goblin stares at you impassively, waiting for you to make your next move.''')
        enemy_p = True

    # asks the player how they would like to react and while none of the moves are true, it runs player_stance() to check for their input until they input a correct response. Also displays the player's health and energy.
    print(f'''                    
                  What move would you like to make?                [ Health = {player_hp} ]
              (L)ight attack, (H)eavy attack, or (P)arry?          [ Energy = {player_eg} ]''')
    while player_l_atk == False and player_h_atk == False and player_p == False:
        x = player_stance()
        if x == 'L':
            player_l_atk = True
        elif x == 'H':
            player_h_atk = True
        elif x == 'P':
            player_p = True

    # all the combinations of player and enemy attacks. Rolls a 3 sided dice to see which dialogue it uses.
    if enemy_l_atk == True and player_l_atk == True:
        rand_num = rand_1_3()
        if rand_num == 1:
            print('You both strike each other with a quick jab, drawing a small amount of blood.')
        elif rand_num == 2:
            print("The goblin and you strike at the same instant, and you each hold a quivering blade, point stuck in the other's chest")
        elif rand_num == 3:
            print('''The goblin darts forward with a lightning fast jab, 
it is too fast to dodge so steel yourself for its impact and stab at the goblin.''')
        pause = input('')
        player_hp -= 1
        enemy_hp -= 1
    elif enemy_l_atk == True and player_h_atk == True:
        rand_num = rand_1_3()
        if rand_num == 1:
            print('You prepare for a heavy strike, but the goblin darts in with a quick jab before you can react.')
        elif rand_num == 2:
            print('You bring your sword high for a mighty blow, but the goblin lunges in with a quick stab before you can swing.')
        elif rand_num == 3:
            print('''With a mighty roar, you swing your sword in a powerful stroke, 
but the goblin darts to the side and stabs you, halting your swing.''')
        pause = input('')
        player_hp -= 1
        player_eg -= 3
        if player_eg < 0:
            player_hp += player_eg
            player_eg = 0
    elif enemy_l_atk == True and player_p == True:
        rand_num = rand_1_3()
        if rand_num == 1:
            print('The goblin strikes at you with a quick jab, but you easily parry the light blow, striking back with a stab.')
        elif rand_num == 2:
            print("Ready for the goblin's swing, you easily parry his blade and strike back with a riposte.")
        elif rand_num == 3:
            print('''The goblin darts in with a quick jab, but you were prepared, 
your sword clashes with the cleaver and slides past to stab the goblin.''')
        pause = input('')
        player_eg -= 1
        if player_eg < 0:
            player_hp += player_eg
            player_eg = 0
        enemy_hp -= 1
    elif enemy_h_atk == True and player_l_atk == True:
        rand_num = rand_1_3()
        if rand_num == 1:
            print('''The goblin lifts his cleaver high, preparing for a mighty strike, 
but you dart in a quick jab before before he can react.''')
        elif rand_num == 2:
            print('''With a roar the goblin charges, his cleaver held high, but you are prepared, 
and with a quick sidestep and jab, the goblin halts with your sword point in his breast.''')
        elif rand_num == 3:
            print('''The goblin braces himself before lunging forward with a mighty blow, 
but you anticipated this and quickly dash to the side, slashing the goblin as he passes by.''')
        pause = input('')
        enemy_hp -= 1
        enemy_eg -= 3
        if enemy_eg < 0:
            enemy_hp += enemy_eg
            enemy_eg = 0
    elif enemy_h_atk == True and player_h_atk == True:
        rand_num = rand_1_3()
        if rand_num == 1:
            print('You both lift your weapons high and strike a vicious blow on each other, disregarding your personal safety.')
        elif rand_num == 2:
            print("With bestial roars, you and goblin lunge at each other, striking mortal blows.")
        elif rand_num == 3:
            print('''Safety be damned! You bound forward with a mighty strike, disregarding the goblin's vicious cleaver, 
and your sword sinks home in your enemy's flesh, while his sinks home in yours.''')
        pause = input('')
        player_hp -= 3
        player_eg -= 3
        if player_eg < 0:
            player_hp += player_eg
            player_eg = 0
        enemy_hp -= 3
        enemy_eg -= 3
        if enemy_eg < 0:
            enemy_hp += enemy_eg
            enemy_eg = 0
    elif enemy_h_atk == True and player_p == True:
        rand_num = rand_1_3()
        if rand_num == 1:
            print('The goblin strikes with a mighty blow, powering through your parry.')
        elif rand_num == 2:
            print('''The goblin lunges at you with a powerful swing, 
you attempt to parry it but the blow is too strong and slides past your blade into your flesh.''')
        elif rand_num == 3:
            print('''The goblin jumps high, cleaver held above his head. You brace yourself and attempt to parry his blow, 
but his momentum is too great and you crumple before his blow, sinking to the ground with a mighty wound.''')
        pause = input('')
        player_hp -= 2
        player_eg -= 1
        if player_eg < 0:
            player_hp += player_eg
            player_eg = 0
        enemy_eg -= 3
        if enemy_eg < 0:
            enemy_hp += enemy_eg
            enemy_eg = 0
    elif enemy_p == True and player_l_atk == True:
        rand_num = rand_1_3()
        if rand_num == 1:
            print("You stab at the goblin with a light strike, but he easily parries the blow and lands a quick riposte.")
        elif rand_num == 2:
            print('''The goblin halts his onslaught and you take the opportunity for a quick strike, 
but he anticipated this and easily parries your blade, striking back with a riposte.''')
        elif rand_num == 3:
            print('''You attempt to dart in a quick strike while the goblin catches his breath, 
but with deceptive speed, the goblin raises his cleaver and parries your blade, striking back with a riposte.''')
        pause = input("")
        player_hp -= 1
        enemy_eg -= 1
        if enemy_eg < 0:
            enemy_hp += enemy_eg
            enemy_eg = 0
    elif enemy_p == True and player_h_atk == True:
        rand_num = rand_1_3()
        if rand_num == 1:
            print('''Your lift your sword over your head and bring it down upon the goblin with a mighty blow, 
he tries to parry the blade, but it powers through and bites into his flesh.''')
        elif rand_num == 2:
            print('''You bound forward with a mighty roar and crush the goblin's blade back in a shower of sparks, 
smashing your sword into his shoulder.''')
        elif rand_num == 3:
            print('''You brace your legs before lunging forward with a mighty stab. 
The goblin's attempt to parry does nothing to stop your blade and it meets home solidly in his chest.''')
        pause = input("")
        player_eg -= 3
        if player_eg < 0:
            player_hp += player_eg
            player_eg = 0
        enemy_hp -= 2
        enemy_eg -= 1
        if enemy_eg < 0:
            enemy_hp += enemy_eg
            enemy_eg = 0
    elif enemy_p == True and player_p == True:
        pause = input("You both steel yourself for an attack, nothing happens.")
    else:
        print(enemy_l_atk, enemy_h_atk, enemy_p, player_l_atk, player_h_atk, player_p)
        pause = input('error in player and enemy attack combination')
    if player_hp <= 0:
        clear_screen()
        end = input(game_over)
        quit()
    if enemy_hp <= 0:
        clear_screen()
        print(goblin_dead)
        pause = input('')
        clear_screen()
        print(treasure_room)
        pause = input('''You enter into the room behind the goblin. 
Torches set on the far wall illuminate a lavishly furnished room filled with various trinkets glittering in the light. 
(Press enter to investigate further...)''')
        pause = input('''
As you walk forward, footfalls dulled by the magnificently spun carpet covering the floor, 
your eyes are drawn to the far end of the room.
Seated upon a marble dais rests the mythical lost crown of Seketh, 
an impossibly smooth circle of diamond set with gleaming gemstones resting beneath the piercing Eye of Seketh.
With this crown you wield the power to rule the world. How will you use it?        
        ''')
        quit()

# the standard order of functions for moving around the map
def order_of_play(room):
    move_char()
    clear_screen()
    stats()
    return_stored(room)
    update_char(room)
    print_room(room)
    print_lines(lines)

# lets you play the game, you just lost the game btw.
def play_game(room):
    menu()
    start = input('(Press enter to continue...)')
    clear_screen()
    stats()
    update_char(room)
    print_room(room)
    playing = True
    while playing:
       order_of_play(room)

#starts the game
play_game(room1)
