def main():
    n = int(input())
    k = int(input())
    vastaus = []

    for x in range(0,n):
        if isPrime(x):
            vastaus.append(x)

    vastaus = vastaus[0::k]
    for x in vastaus:
        print(x, end=' ')
    print()

def isPrime(i):
    if i < 2:
        return False
    for x in range(2, i):
        if not( i % x ):
            return False
    return True

main()
