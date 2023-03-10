def fibonacciCheck(checkValue):
    if checkValue == 0:
        return True
    
    fibonacciValues = [0,1]
    while checkValue > fibonacciValues[1]:
        fibonacciValues = fibonacciValues[1], sum(fibonacciValues)

    if checkValue == fibonacciValues[1]:
        return True
    
    return False

input = 1304969544928657

if fibonacciCheck(input):
    print("O valor ", input, " faz parte da sequencia Fibonacci!")
else:
    print("O valor ", input, " NÃO faz parte da sequencia Fibonacci!")