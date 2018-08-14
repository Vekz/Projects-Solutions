def findDigPi():
    
    try:
        decPlace = input("Enter to which decimal place Pi is going to be
                         printed. ")
        decPlace = int(decPlace)
    except ValueError:
        print("You didn't enter an integer")
        return 0
    
    
    with open('100000_digits_of_PI.txt') as Pile:
        ''' File contains 100 000 digits of PI,
        credits to:
        http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
        It's faster than calculating PI every time using e.g. Nilakantha
        Series '''
        Pi = Pile.read(decPlace+2)
    Pile.closed
    

    ''' If you want to use Nilakantha Series instead of using precalculeted Pi
    from the file uncomment next block and comment previous block '''
    
     
    # def NilakanthaSeries(iter):
    #     ''' Iter says how deep in calculating this series you will go e.g.
    #     100 is 50 additions and 50 subtractions, and it returns accurate Pi to
    #     3.14159 '''
    #     Pi = 3
    #     for num in range(2,iter,2):
    #         if (num%4 == 0):
    #             Pi -= (4/(num*(num+1)*(num+2)))
    #         else:
    #             Pi += (4/(num*(num+1)*(num+2)))
    #     return Pi
        
    # iterations = 100
    # Pi = NilakanthaSeries(iterations)
    # Pi = round(Pi, decPlace)
    
    
    return Pi

print(findDigPi())
