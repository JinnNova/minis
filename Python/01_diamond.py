# Not so useful Python minis by Hanna "Jinn" Enqvist

def main():
    h = input("Give an odd number: ")
    while h:
        h = int(h)
        s = str(input("Give a character:"))

        drawDiamond(h,s)

        print()
        h = input("Give an odd number, or press enter to quit: ")

def drawDiamond(h,s):
    rivit = [s]
    for x in range(1,h,2):
        rivit.append(s + " " * x + s)
    rivit += rivit[:-1][::-1]

    keskita = lambda x: ('{:^%s}' % h).format(x)
    diamond = '\n'.join(map(keskita, rivit))
    print(diamond)
    
    return

main()
