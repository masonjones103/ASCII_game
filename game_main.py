''' Hello, this is the starting code for my WIP ASCII game.

#TO-DO:
 - FIX: Occasional Out-Of-Bounds Error(?)
 - Add treasure room
 - Add new equipment
#DOING:
 -Adding combat and making the goblin in ASCII

#DONE:
 - Added bounds to the room
 - Added collision to enemy
'''

import os

# stores the row and index of the player character. [4, 3] is the starting position of the '@' character.
position = [4, 3]

# stores the symbol the player walks over so it can be returned after they walk off.
stored_char = [4, 3, ' ']

# room stored as nested lists
room1 = [
         ['[', '=', '=', '-', '=', '=', ']'],
         ['[', ' ', ' ', 'g', ' ', '^', ']'],
         ['[', '^', ' ', ' ', ' ', ' ', ']'],
         ['[', ' ', ' ', ' ', ' ', '^', ']'],
         ['[', '^', ' ', ' ', ' ', ' ', ']'],
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

# a very scary goblin. For some reason line 47 reads normal if the terminal if I run it offset like that.
goblin = r'''
                            /\     /\
	                   (  \___/  )
                            |       |
                            \ o' 'o /
                             | """ |     __
                     ^^      \ """ /     \_\
                     \ \      |   |      /  |  
                      \ \____/     \____/ /\ \_
                       \_____ .   . _____/  \  |>
                            /       \        \  |>
                           /    .    \        \  |>
                          {----(#)----}        \/
                          {           }
                          {_/\_____/\_}
                            ||     ||
                            (|     |)
                            ||     ||
                           /  \   /  \
                           ^^^^   ^^^^
                           
            You meet face to face with the ferocious goblin.
              Will you (A)ttack the goblin or (R)un away?
'''

# the player's stat values
hp = 10
dmg = 1
weapon = 'Sword'
armor = 'Leather'

# set to False if the goblin dies
enemy_alive = True

# stores lines that happened upon certain conditions
lines = ['']

# prints a menu where the player can select to play or exit the game
def menu():
    print('>----------<')
    print('(P)lay')
    print('(E)xit')
    print('>----------<')
    play = False
    exit_menu = False
    while play == False and exit_menu == False:
        menu_choice = input('>').lower().strip()
        if menu_choice == 'p':
            play = True
        elif menu_choice == 'e':
            exit_menu = True
        else:
            print('Please type (P) to play or (E) to exit.')
    if play:
        print('''Welcome to the Dungeon of Doom...
You enter a damp, musty room, water drips from the ceiling and torches set upon its walls grant a flicking light.
You see a shape looming in the distance, a menacing goblin with a vicious cleaver guards the far door.
You grasp your sword and move forward cautiously...''')
    elif exit_menu:
        quit()

# prints stat menu, uses .ljust to keep boundaries even regardless of variable length
def stats():
    print('[====================]')
    print(f'[ HP = {hp}          '.ljust(21, ' '), end='')
    print(']')
    print(f'[ DMG = {dmg}        '.ljust(21, ' '), end='')
    print(']')
    print(f'[ Weapon = {weapon}  '.ljust(21, ' '), end='')
    print(']')
    print(f'[ Armor = {armor}    '.ljust(21, ' '), end='')
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

# temporary win condition if you make it to the end of the room.
def win_game():
    if position == [0, 3]:
        pause = input("Congrats! You've completed the game!")
        exit()

# stored in lines if you encounter the goblin
def on_enemy():
    lines[0] = 'You meet face to face with the ferocious goblin.'

# prints stored lines, then clears the lines list.
def print_lines(lines):
    for line in lines:
        print(line)
        print('')
    lines[0] = ''

# updates the position list to give coordinates that your character will move to when update_char() is called.
def move_char():
    new_position = [4, 3]   # where the player is trying to move, does not actually move there unless check_bound() returns False
    previous_position = [4, 3]  # where the player was standing before checking if a wall was in the way.
    previous_position[0] = position[0]
    previous_position[1] = position [1]
    move_input = input("Press 'W' to move forward, 'S' to move back, 'A' to move left, or 'D' to move right.\n>").upper().strip()
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
            combat()
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
            combat()
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
            combat()
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
            combat()
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

# if you encounter the goblin, this function clears the screen and prints the scary goblin
def combat():
    clear_screen()
    print(goblin)
    choice1 = input('>').upper().strip()
    if choice1 == 'A':
        print("You stab the poor goblin through the heart and exit through the door behind it.")
        pause = input("Congrats! You've won the game!")
        quit()
    elif choice1 == 'R':
        print("You turn around to run, the goblin lunges onto your back and stabs you repeatedly until you die.")
        print("Game over...")
        pause = input('')
        quit()
    else:
        combat()

# the standard order of functions for moving around the map
def order_of_play(room):
    move_char()
    clear_screen()
    stats()
    return_stored(room)
    update_char(room)
    print_room(room)
    print_lines(lines)
    win_game()

# lets you play the game, you just lost the game btw.
def play_game(room):
    menu()
    start = input('Press enter to continue...')
    clear_screen()
    stats()
    update_char(room)
    print_room(room)
    playing = True
    while playing:
       order_of_play(room)

#starts the game
play_game(room1)
