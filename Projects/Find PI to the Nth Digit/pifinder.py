
try:
    decPlace = input("Enter to which decimal place Pi is going to be printed.")
    decPlace = int(decPlace)
except ValueError:
    print("You didn't enter an integer")
    exit()

with open('100000 digits of PI.txt') as Pile:
    ''' File contains 100 000 digits of PI,
    credits to: http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
    It's faster than calculating PI every time using e.g. Nilakantha Series '''
    Pi = Pile.read(decPlace+2)
Pile.closed

print(Pi)


