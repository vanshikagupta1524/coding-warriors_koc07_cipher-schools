print("You Have Three chances to Guess.")
import random
a = range(10)
b = random.choice(a)
c = int(input("Enter your first guess:"))
d = int(input("Enter your second Guess:"))
f = int(input("Enter Your Third Guess:"))
if c == b:
    print("You Won")
    print(b)
elif d == b:
    print("You won")
    print(b)
elif f == b:
    print("you won")
    print(b)
else:
    print("Better Luck next time")
    print(b)