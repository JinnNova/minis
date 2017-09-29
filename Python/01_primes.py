# Not so useful Python minis by Hanna "Jinn" Enqvist

def main():
    n = int(input("Print primes up to number X (Give a whole number X): "))
    k = int(input("Print every N:th prime number. (Give N): "))
    vastaus = []

    for x in range(0,n):
        if isPrime(x):
            vastaus.append(x)
            
    # Splitting the list of primes
    vastaus = vastaus[0::k]
    for x in vastaus:
        print(x, end=' ')
    print()

# checking if a number is Prime
def isPrime(i):
    if i < 2:
        return False
    for x in range(2, i):
        if not( i % x ):
            return False
    return True

main()
