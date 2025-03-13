import random
import os
import time
print("Memory Game")
def get_numbers():
    while True:
            x = 0
            listtouse = [] #list to append to
            while x < 4:
                listtouse.append(random.randint(1,17)) #generate random number between 1-17 and place it in a list
                x+=1 
            counter = len(set(listtouse))
            if counter >= 4:
                return listtouse
def shownum():
    print("""
        1 2 3 4
        5 6 7 8
        9 10 11
        12 13 14
        15 16 17
    """)

wins = 0
playnum = 0
def main():
    global wins
    global playnum
    os.system("cls")
    try:
        winpercent = wins/playnum * 100
    except ZeroDivisionError:
        print(r"You have won 100% of the games.")
    else:
        print(f"You have won {winpercent}% of the games so far.")
    print(f"You have won {wins} games so far.")
    shownum()
    print("You'll be given 4 numbers, and you have to remember them, then you'll be asked about what numbers to remember.")
    numbers = get_numbers()
    print(' '.join(map(str, numbers)))
    time.sleep(5)
    os.system("cls")
    print("What were the numbers?")
    user_numbers = []
    for i in range(1, 5):
        try:
            num = int(input(f"Number {i}: ").strip())
            user_numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a number.")
            return
    if sorted(user_numbers) == sorted(numbers):
        print("Round succeeded!")
        wins+=1
        playnum+=1
        time.sleep(3)
    else:
        print("You missed some numbers or entered incorrectly. Try again.")
        time.sleep(3)
        playnum+=1
        return
if __name__ == "__main__":
    while True:
        main()