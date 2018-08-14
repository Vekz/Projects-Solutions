def getFibonacciToNthNumber(N):
    fib = [0,1]
    for x in range(2,N):
        fib.append(fib[x-2]+fib[x-1])
    return fib

def fibo():
    try:
        howMany = input("How many Fibonacci numbers would you like to see: ")
        howMany = int(howMany)
    except ValueError:
        print("You didn't enter an positive integer")
        return 0

    print(getFibonacciToNthNumber(howMany))

fibo()