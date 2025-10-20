# define a function that takes n and return true or false based on min and max allowed range
def not_in_range(n):
    return True if min_n <= n <= max_n else False

# defining and seting the n, max and min n for the program:
min_n, max_n, input_n = 1, 10, -1


#printing a welcome message:
print('Welcome to checking input validation program')

while not not_in_range(input_n):
    input_str = input('Pick an integer between ' + f'{min_n} and {max_n}:  ')

    try:
        input_n = int(input_str)
    except ValueError:
        print('You did not enter a valid integer')
    else:
        if not_in_range(input_n):
            print('Your integer is between ' + f'{min_n} and {max_n}')
        else:
            print('Your integer is not between ' + f'{min_n} and {max_n}')

print('Program completed. you chose: ', input_n)
