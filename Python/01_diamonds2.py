# Not so useful Python minis by Hanna "Jinn" Enqvist

def main():
    h = input("Give an odd number (height of the diamond): ")
    while h:
        h = int(h)
        n = input("Give a number of diamonds (1-10): ")
        n = int(n)
        s = str(input("Give a character: "))

        drawDiamond(h,s,n)

        print()
        h = input("Give an odd number, or press enter to quit: ")

def drawDiamond(h,s,n):
    rivit = [s]
    for x in range(1,h,2):
        rivit.append(s + " " * x + s)

    rivit += rivit[:-1][::-1]

    for rivi in rivit:
        for y in range (0,n):
            if y < n-1:
                # Easier way to center stuff in Python
                print(rivi.center(h," "), end=" ")
            else:
                print(rivi.center(h," "))
    return
main()
