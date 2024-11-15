''' Hello, this is the starting code for my WIP ASCII game.

#TO-DO:
 - FIX: Occasional Out-Of-Bounds Error(?)
 - Add bounds to the room
#DOING:
 - 

#DONE:
 -

'''

#import os

#stores the row and index of the player character. [4, 3] is the starting position of the '@' character.
position = [4, 3]
stored_char = [4, 3, ' ']

#the player's stat values
hp = 10
dmg = 1
weapon = 'Club'
armor = 'Leather'

#prints a menu where the player can select to play or exit the game
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
        print('Welcome to the Dungeon of Doom...')
    elif exit_menu:
        quit()

#prints stat menu, uses .ljust to keep boundaries even regardless of variable length
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

#takes the room number, then prints each character in a row, iterates to the next row, and continues until all rows are printed.
def print_room(room):
    for row in room:
        print('')
        for char in row:
            print(char, end='')
    print('''
    ''')

#takes the room, row, and index numbers and changes the given spot to the char.
def change_char(room, row, index, char):
    value = True
    while value:
        room[row][index] = char
        value = False

def move_char():
    move_input = input("Press 'W' to move forward, 'S' to move back, 'A' to move left, or 'D' to move right.\n>").upper().strip()
    if move_input == 'W':
        position[0] = position[0] - 1
    elif move_input == 'S':
        position[0] = position[0] + 1
    elif move_input == 'A':
        position[1] = position[1] -1
    elif move_input == 'D':
        position[1] = position[1] + 1
    else:
        move_char()

def update_char(room):
    row = position[0]
    char = position[1]
    stored_char[0] = position[0]
    stored_char[1] = position[1]
    stored_char[2] = room[row][char]
    room[row][char] = '@'

def return_stored(room):
    row = stored_char[0]
    char = stored_char[1]
    symbol = stored_char[2]
    room[row][char] = symbol

def play_game(room):
    menu()
    stats()
    update_char(room)
    print_room(room)
    playing = True
    while playing:
        move_char()
        return_stored(room)
        update_char(room)
        print_room(room)

room1 = [['[', '=', '=', '-', '=', '=', ']'],
         ['[', ' ', ' ', 'g', ' ', '^', ']'],
         ['[', '^', ' ', ' ', ' ', ' ', ']'],
         ['[', ' ', ' ', ' ', ' ', '^', ']'],
         ['[', '^', ' ', ' ', ' ', ' ', ']'],
         ['[', '=', '=', '-', '=', '=', ']'],
         ]

play_game(room1)
