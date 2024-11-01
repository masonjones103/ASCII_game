# Hello, this is the starting code for my WIP ASCII game.

#import os

hp = 10
dmg = 1
weapon = 'Club'
armor = 'Leather'

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

#accesses the nested list to print each character in the chosen list
def print_room(room, row):
    i = 0
    for char in range(len(room[row])):
        print(room[row][i], end='')
        i += 1
    print('')

#calls print_row to print multiple rows, need to figure out how to iterate through each row
# def print_room(row):
#     #row_num = 1
#     for row_num in range(1):
#         print_row(row)
#         print('')
#         #row_num += 1

#updates the inputted row index to match the inputted character
def change_char(row, index, char):
    value = True
    while value:
        row[index] = char
        #print_row(row)
        #print('')
        value = False

# def player_cords(room, row, index):
#     if room1.find('@') != -1:
#         player_position = room[row][index]
#         return player_position

#searches each row to see if the '@' character is found. If it is, it returns that index, else it returns -1
def find_row(row):
    search = True
    while search:
        try:
            return room1[row].index('@')
        except ValueError:
            return -1

#iterates through each row, then uses find row to find the index of '@'
def find_pos():
    row = 0
    pos = 0
    search = True
    while search:
        if find_row(row) == -1:
            row += 1
            find_row(row)
        else:
            pos = find_row(row)
            return pos

#def update_position():

#def clear_row():

#the stored rows in a list, I'm hoping to use these to refresh screen to erase previous prints
row1 = ['[', '=', '=', '-', '=', '=', ']']
row2 = ['[', ' ', ' ', ' ', ' ', ' ', ']']
#used to store the changed character
updated_row1 = ['[', '=', '=', '-', '=', '=', ']']
updated_row2 = ['[', ' ', ' ', ' ', ' ', ' ', ']']

room1 = [['[', '=', '=', '-', '=', '=', ']'],
         ['[', ' ', ' ', ' ', '@', ' ', ']'],
         ]
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
# menu()
# stats()
# end = input('')
print_room(room1, 0)
print_room(room1, 1)
#print(player_cords(room1, 1, 3))
test_list = ['=', '@', '=']
# print(test_list.index('@'))
# print(room1[1].index('@'))
print(find_pos())
