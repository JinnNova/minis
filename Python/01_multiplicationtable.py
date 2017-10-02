a = int(input())
b = int(input())
c = int(input())
d = int(input())

#lasketaan solun maksimikoko, joka on b*d merkkijonon pituus +1
solunleveys = len(str(b*d))+1 

#taulukon otsikkorivin tulostus
print(" " * solunleveys, end="")
for x in range(a,b+1):
    strX = str(x)
    print(" " * (solunleveys - len(strX)) + strX, end="")
print()

#Kertotaulun lukujen tulostus
for y in range(c,d+1):
    strY = str(y)
    print(" " * (solunleveys - len(strY)) + strY, end="")
    for z in range(a,b+1):
        strNum = str( y * z )
        #printataan tarvittava määrä spacea aina ennen lukua
        print(" " * (solunleveys - len(strNum)) + strNum, end="")
    print()
