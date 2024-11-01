# Hello, this is the starting code for my WIP ASCII game.

# room1 = [
#         ['[', '=', '=', '-', '-', '=', '=', ']'],
#         ['[', ' ', ' ', ' ', ' ', ' ', ' ', ']'],
#         ['[', ' ', ' ', ' ', ' ', ' ', ' ', ']'],
#         ['[', ' ', ' ', ' ', ' ', ' ', ' ', ']'],
#         ['[', ' ', ' ', ' ', ' ', ' ', ' ', ']'],
#         ['[', '=', '=', '=', '=', '=', '=', ']'],
#         ]
#prints each individual character in a row using a for loop
import os

hp = 10
dmg = 1
weapon = 'Club'
armor = 'Leather'

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

def menu():
    print('>----------<')
    print('(P)lay')
    print('(E)xit')
    print('>----------<')
    Play = False
    Exit = False
    while Play == False and Exit == False:
        menu_choice = input('>').lower().strip()
        if menu_choice == 'p':
            Play = True
        elif menu_choice == 'e':
            Exit = True
        else:
            print('Please type (P) to play or (E) to exit.')
    if Play == True:
        print('Welcome to the Dungeon of Doom...')
    elif Exit == True:
        quit()

def print_row(row):
    for char in row:
        print(char, end='')

#calls print_row to print multiple rows, need to figure out how to iterate through each row
def print_room(row):
    #row_num = 1
    for row_num in range(1):
        print_row(row)
        print('')
        #row_num += 1

#updates the inputted row index to match the inputted character
def change_char(row, index, char):
    value = True
    while value:
        row[index] = char
        #print_row(row)
        #print('')
        value = False

#def update_position():

#def clear_row():

#the stored rows in a list, I'm hoping to use these to refresh screen to erase previous prints
row1 = ['[', '=', '=', '-', '=', '=', ']']
row2 = ['[', ' ', ' ', ' ', ' ', ' ', ']']
#used to store the changed character
updated_row1 = ['[', '=', '=', '-', '=', '=', ']']
updated_row2 = ['[', ' ', ' ', ' ', ' ', ' ', ']']
# for char in room1:
#     print(char, end='')
# for char in room2:
#     print(char)

# print_room(row1)
# change_char(updated_row2, 2, '@')
# print_room(updated_row2)
# updated_row2 = row2
# change_char(updated_row2, 3, '@')
# print_room(updated_row2)
menu()
stats()
end = input('')