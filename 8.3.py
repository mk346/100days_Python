#prime number check
n = int(input("Enter the number to check: "))

def prime_checker(number_n):
    is_prime = True
    if number_n <= 1:
        is_prime = False
    for i in range(2, number_n): #get numbers all between 2 and the number
        if number_n % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number_n} is a prime number")
    else:
        print(f"{number_n} is not a prime number")
    
    
prime_checker(number_n = n)