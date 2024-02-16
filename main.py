import os
import time


def print_drinks(drinks):
    print("**************************************************")
    print("Here is a selection of Batu Roasteria's coffees:")
    j = 1
    for val in drinks:
        print(f'{j}. {val} ${drinks[val]}')
        j += 1
    print("**************************************************")


def print_coworkers(workers):
    print("**************************************************")
    print("Coworkers:")
    for val in workers:
        print(val)
    print("**************************************************")


def print_coworkers_with_spent(workers):
    print("**************************************************")
    print("Coworkers:")
    for val in workers:
        print(f'{val} has spent ${workers[val]}')
    print("**************************************************")

def find_key_with_min(workers):
    res = "Bob"
    val = workers["Bob"]
    for key in workers:
        if workers[key] < val:
            val = workers[key]
            res = key
    return res

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


clear()

workers = {
    "Bob": 0,
    "Jeremy": 0
}

confirmed = False

while not confirmed:
    print("Please enter the other 5 coworkers' names!")
    for i in range(5):
        worker = input(f'Please enter name of coworker {i+3}: ')
        workers[worker] = 0
    clear()
    print_coworkers(workers)
    choice = input("Confirm coworkers [y/N]: ")
    if choice == "y":
        confirmed = True
    else:
        workers = {
            "Bob": 0,
            "Jeremy": 0
        }

drinks = {
    "Black": 2.00,
    "Americano": 2.75,
    "Espresso": 2.50,
    "Latte": 3.50,
    "Cappucino": 3.25,
    "Cold Brew": 3.00
}

clear()
print_drinks(drinks)

choice = input("Do you want to add more drinks [y/N]: ")
while choice == "y":
    print("Please either use just words for the name of the drink or floating point number.")
    try:
        name = input("Please input the name of the drink: ").capitalize()
        price = float(input(f"Please input the price of {name}: "))
        drinks[name] = price
    except:
        print("Wrong choice of input!")
        time.sleep(2)
    clear()
    print_drinks(drinks)
    choice = input("Do you want to add more drinks [y/N]: ")

clear()
i = 1
done = False
total = 0
while not done:
    clear()
    print(f'Day {i}')
    print_coworkers_with_spent(workers)
    time.sleep(3)
    clear()
    print_drinks(drinks)

    for key in workers:
        if key == "Bob":
            print("\nBob gets the cappucino as always.\n")
            total += drinks["Cappucino"]
        else:
            if key == "Jeremy":
                print("Jeremy likes his coffee black. I know he would like the espresso or an americano.\n")
            print(f"What will {key} pick?\n")
            correct = False

            while not correct:
                try:
                    choice = int(input("Choice (input an integer e.g 1): "))
                    drink = list(drinks.keys())[choice-1]
                    correct = True
                except:
                    print("Wrong input, try again!")
    
    print(f'\n{key} gets the {drink}.\n')
    total += drinks[drink]
    who_pays = find_key_with_min(workers)
    print(f'{who_pays} pays the bill of {total}')
    time.sleep(3)
    workers[who_pays] += total
    total = 0
    i += 1

