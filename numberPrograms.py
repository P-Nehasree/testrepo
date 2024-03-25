
'''n = 100
prime = []
num = 2

for _ in range(n):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)
    num += 1

print(prime) '''

'''

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries as true. A value in prime[i] will finally
    # be false if i is Not a prime, else true.
    prime = [True for _ in range(n+1)]
    p = 2
    while p**2 <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes

# Example usage:
N = 100
print("Prime numbers between 1 and", N, "are:", sieve_of_eratosthenes(N))
'''

#chatgpt

'''
def is_armstrong(num):
    # Calculate the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    return armstrong_sum == num

def first_n_armstrong_numbers(N):
    armstrong_numbers = []
    num = 0
    
    # Keep checking numbers until we find N Armstrong numbers
    while len(armstrong_numbers) < N:
        num += 1
        if is_armstrong(num):
            armstrong_numbers.append(num)
    
    return armstrong_numbers

# Example usage:
N = 10
print(f"The first {N} Armstrong numbers are:", first_n_armstrong_numbers(N))

'''
#chat gpt code 2
'''
def is_armstrong(number):
    # Calculate the number of digits in the number
    num_digits = len(str(number))
    # Calculate the sum of each digit raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in str(number))
    # Check if the total is equal to the original number
    return total == number

def print_armstrong_numbers(N):
    armstrong_numbers = []
    for i in range(1, N + 1):
        if is_armstrong(i):
            armstrong_numbers.append(i)
    return armstrong_numbers

# Example usage:
N = 1000
print("Armstrong numbers between 1 and", N, "are:", print_armstrong_numbers(N))

'''

#Perfect number
#Chat gpt code

'''
def sum_of_divisors(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum

def print_perfect_numbers(N):
    perfect_numbers = []
    for i in range(1, N + 1):
        if sum_of_divisors(i) == i:
            perfect_numbers.append(i)
    return perfect_numbers

# Example usage:
N = 1000
print("Perfect numbers between 1 and", N, "are:", print_perfect_numbers(N))

'''

#Perfect number upto given N value
sum=0
n=1
for _ in range(1000):
    p=n
    sum=0
    for i in range(1,n):
        
        if n%i==0:
            sum=sum+i
    if sum==p:
        print(n)
    n=n+1

# Prime numbers within the range
n=2
for _ in range(1000):
    
    p=n
    c=0
    for i in range(1,n+1):
        if p%i==0:
            c=c+1
    if c==2:
        print(p,end=" ")
    n=n+1
