import math

def findDigE():
    
    try:
        decPlace = input("To which decimal place e should be printed: ")
        decPlace = int(decPlace)
    except ValueError:
        print("You didn't enter an integer")
        return 0

    with open('1M_digits_of_e.txt') as Eile:
        ''' File contains 1 million digits of e,
        credits to: https://apod.nasa.gov/htmltest/gifcity/e.1mil,
        NASA, Robert Nemiroff and Jerry Bonnell.
        It's faster than calculating e every time using e.g Brothers' Formulae 
        '''
        e = Eile.read(decPlace+2)
    Eile.closed

    ''' If you want to use Brothers' Formulae instead of using precalculeted e
    from the file uncomment next block and comment previous block '''

    # def BrothersFormulae(steps):
    #     ''' Steps says how deep in calculating this series you will go e.g.
    #     with only 6 steps you have 9 accurate decimal places '''
    #     e = 0
    #     for n in range(steps+1):
    #         e += (2*n+2)/math.factorial(2*n+1)
    #     return e

    # e = 1000
    # e = BrothersFormulae(steps)
    # e = round(e,decPlace)

    return e

print(findDigE())
