# Not so useful Python minis by Hanna "Jinn" Enqvist

shakkiRivi = []

ruutuMaaraRows = int(input("Give the number of squares per row: "))
ruutuMaaraCols = int(input("Give the number of squares per column: "))

ruudunKorkeus = int(input("Give the height of one square: "))
ruudunLeveys = int(input("Give the width of one square: "))

for r in range(0,ruutuMaaraRows):
    for z in range(0,ruudunKorkeus):
        # Emptying the row each time before filling it up with characters
        shakkiRivi = []
        for y in range(0,ruutuMaaraCols):
            for x in range(0,ruudunLeveys):
                # If Row = Even and Squarenumber = Even, OR Row = Odd and Squarenumber = Odd
                if ((r % 2 == 0 and y % 2 == 0) or (r % 2 != 0 and y % 2 != 0)):
                    shakkiRivi.append(" ")
                # If Row = Even and Squarenumber = Odd, OR Row = Odd and Squarenumber = Even
                if ((r % 2 == 0 and y % 2 != 0) or (r % 2 != 0 and y % 2 == 0)):
                    shakkiRivi.append("#")
        for l in shakkiRivi:
            print(l,end="")
        print()


