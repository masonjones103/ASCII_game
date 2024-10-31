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

# for char in room1:
#     print(char, end='')
# for char in room2:
#     print(char)

print_room(row1)
change_char(updated_row1, 3, '@')
print_room(updated_row1)
change_char(updated_row1, 4, '@')
print_room(updated_row1)