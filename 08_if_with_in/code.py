# number = 8
# user_input = input('Enter "y" if you would like to play: ')

# if user_input == 'y':
#     user_number = int(input("Guess my number: "))
#     if user_number == number:
#         print('You guessed corretly')

#     else:
#         print("Sorry , it is wrong")


# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if (number % 2 == 0):
        evens.append(number)
        print(evens)


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == 'q':
    print("Quit")
