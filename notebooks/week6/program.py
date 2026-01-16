# Integer to binary
def to_binary(n: int) -> str:
    if n <= 0:
        return "Error: enter a positive integer"
    return bin(n)[2:]  

# tests
print(to_binary(1))
print(to_binary(10))   
print(to_binary(64))

# Factors
def factors(n: int) -> list[int]:
    if n == 0:
        return []
    n = abs(n)
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


print(factors(10))    
print(factors(16))   
print(factors(-15)) 

# This program checks whether number is prime or not 
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


print(is_prime(5))   
print(is_prime(20))   
print(is_prime(13))  
print(is_prime(21)) 

# Remove spaces and reverse output
def encrypt_reverse_no_spaces(message: str) -> str:
    no_spaces = message.replace(" ", "")
    return no_spaces[::-1]


print(encrypt_reverse_no_spaces("hello world"))  
print(encrypt_reverse_no_spaces("say hi”)) 














