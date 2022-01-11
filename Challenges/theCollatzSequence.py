# This program executes the Collatz Sequence

print('What is your number?')

# numero = int(input()) # With integer conversion

numero = (input()) # Without integer conversion to trigger try/except clauses

def collatz (number): # Create a function named Collatz with a paramater named number
    if number % 2 == 0: # If number is even, print number // 2
        number = number // 2
        return number
    elif number % 2 == 1: # If number is odd, print 3 * number + 1
        number = 3 * number + 1
        return number

try:
    while numero != 1: # Loop the function until it returns 1
        numero = collatz (numero)
        print(numero) # Print every step of the loop

except:
    numero != int
    print('Please insert a valid number.')